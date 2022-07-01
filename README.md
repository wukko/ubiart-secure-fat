# ubiart-secure-fat
UbiArt `secure_fat.gf` file generator that is essential for modding any UbiArt game.

## Why?
`secure_fat.gf` file contains a list of file path hashes in each game bundle. UbiArt games use it to locate files and load them. Without editing this file it's impossible to load custom files. This script generates a fresh file that includes all files in official or custom IPK bundles. It has been used personally by me for many years to create mods for Just Dance.

## Supported games
- Just Dance 2015 - 2022 on all platforms (probably Just Dance 2014 too, haven't tested it)
- Rayman Legends
- Rayman Origins
- ...most likely any other UbiArt game in existence

## How to use it
This script doesn't depend on any external modules. All you need is Python 3+.

1. Download `generateSecureFat.py`
2. Copy downloaded file to desired game directory
3. Run it by opening command prompt or terminal in directory and running `py generateSecureFat.py`
4. Boom, you have a perfect `secure_fat.gf` file!

You can also use this script as a module (like I usually do).

## Customization
You can change default values in the `generateSecureFat.py` file to match your modded game.
