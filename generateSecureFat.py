#
# https://github.com/wukko/ubiart-secure-fat
#
# UbiArt secure_fat.gf file generator using existing IPK bundles by https://github.com/wukko
# Tested on Just Dance 2015 - 2022 games on PC, Wii, Wii U, Nintendo Switch (NX).
# This script should work for Rayman Legends/Origins and other UbiArt games too.
#
# This script includes all matching files in current directory and its subdirectories when used standalone. Keep this in mind when using it.
#
# Credit to me (https://github.com/wukko) is required when this script is used in other projects.

import os

# Modify these variables for standalone use if needed
out = "secure_fat.gf"
bext = ".ipk"
ignore = ["patch"]
p = ["pc", "wii", "wiiu", "nx", "x360", "durango", "scarlett", "ps3", "orbis", "prospero", "ggp"]

def nameOnly(name, ext):
    name = name.split('/')[len(name.split('/'))-1]
    for i in p:
        name = name.replace(ext, '').replace('_'+i, '')
    return name

def hashList(input):
    hashes = []
    with open(input, "rb") as f:
        f.read(16)
        filecount = int.from_bytes(f.read(4), "big")
        f.read(40)
        counter = 0
        while counter != filecount:
            f.read(16)
            f.read(int.from_bytes(f.read(4), "big"))
            f.read(int.from_bytes(f.read(4), "big"))
            hashes.append(f.read(4))
            f.read(16)
            counter += 1
    return hashes

def generateSecureFat(cwd, out, bext, ignore):
    bl = []

    for root, dir_names, file_names in os.walk(cwd):
        for f in file_names:
            path = os.path.join(root, f).replace(cwd, '')[1:]
            if path[-4:] == bext:
                bl.append(path)

    bl = [b for b in bl if not nameOnly(b, bext) in ignore]

    with open(out, "wb") as f:
        bundleCount = 0
        hashesCount = 0
        body = b''
        footer = b''
        for i in bl:
            ipkhash = hashList(i)
            hashesCount += len(ipkhash)
            ipkname = nameOnly(i, bext).encode()
            for h in ipkhash:
                body += h + b'\x00\x00\x00\x01' + bundleCount.to_bytes(1, "big")
            footer += bundleCount.to_bytes(1, "big") + len(ipkname).to_bytes(4, "big") + ipkname
            bundleCount = bundleCount + 1
        f.write(b'\x55\x53\x46\x54\x1F\x5E\xE4\x2F\x00\x00\x00\x01' + hashesCount.to_bytes(4, "big"))
        f.write(body)
        f.write(bundleCount.to_bytes(4, "big"))
        f.write(footer)

if __name__ == "__main__":
    generateSecureFat(os.getcwd(), out, bext, ignore)
