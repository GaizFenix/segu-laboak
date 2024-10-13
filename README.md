# Segu-Laboak

This repository contains scripts for steganography and cryptography tasks. The project is divided into two main directories: `Esteganografia` and `Zifraketa`.

## Directory Structure

segu-laboak/ ├── Esteganografia/ │ └── script_v1.py ├── README.md └── Zifraketa/ ├── script_v1.py └── script_v2_ibai.py


## Esteganografia

The `Esteganografia` directory contains scripts related to steganography. Steganography is the practice of hiding secret data within an ordinary, non-secret file or message to avoid detection.

### `script_v1.py`

This script performs the following tasks:
- Computes the MD5 hash of images in a specified directory.
- Compares the computed hash with a known hash to find a matching image.
- Prints the path of the secret image if a match is found.

#### Functions

- `getImgRoute()`: Returns the path to the image directory.
- `computeMD5Hash(image_path)`: Computes the MD5 hash of the given image.
- `hash_images_in_directory(directory, known_hash)`: Computes and prints the MD5 hash of images in the specified directory and checks for a match with the known hash.
- `main()`: Main function that sets up the image directory and known hash, and calls the `hash_images_in_directory` function.

## Zifraketa

The `Zifraketa` directory contains scripts related to cryptography. Cryptography is the practice of securing information by transforming it into an unreadable format, only readable by those possessing a secret key.

### `script_v1.py`

This script performs the following tasks:
- Defines the Spanish alphabet and the percentage of usage of each letter.
- Deciphers a given text file by mapping the most common letters to the most used letters in the Spanish language.
- Allows modification of the usage alphabet by swapping letters.

#### Functions

- `esAlphPerc()`: Returns a dictionary with the Spanish alphabet and their usage percentages.
- `decypher(file_path, usage_alphabet)`: Deciphers the text in the given file using the provided usage alphabet.
- `modify_alphabet(usage_alphabet, letter1, letter2)`: Swaps two letters in the usage alphabet.
- `loop()`: Main loop that reads the text file, deciphers it, and allows for modifications to the usage alphabet.

### `script_v2_ibai.py`

This script is an updated version of `script_v1.py` with additional features and improvements.

## Usage

To run the scripts, navigate to the respective directories and execute the Python scripts using the following commands:

```sh
cd Esteganografia
python [script_v1.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fgaizka%2FDocuments%2Fsegu-laboak%2FEsteganografia%2Fscript_v1.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fgaizka%2FDocuments%2Fsegu-laboak%2FEsteganografia%2Fscript_v1.py%22%2C%22path%22%3A%22%2Fhome%2Fgaizka%2FDocuments%2Fsegu-laboak%2FEsteganografia%2Fscript_v1.py%22%2C%22scheme%22%3A%22file%22%7D%7D)

cd Zifraketa
python [script_v1.py](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fgaizka%2FDocuments%2Fsegu-laboak%2FEsteganografia%2Fscript_v1.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fgaizka%2FDocuments%2Fsegu-laboak%2FEsteganografia%2Fscript_v1.py%22%2C%22path%22%3A%22%2Fhome%2Fgaizka%2FDocuments%2Fsegu-laboak%2FEsteganografia%2Fscript_v1.py%22%2C%22scheme%22%3A%22file%22%7D%7D)


This README provides a clear overview of the project, its directory structure, and the functionality of the scripts within each directory.