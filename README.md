# Decoder
This project performs the decryption of classical ciphers using the Metropolis Algorithm.
## Instructions
* In order to compile the files, you'll need to have [Python](https://www.python.org/downloads/) installed.
* The script used in this project also needs the package `numpy`, which can be added with the following commands:
```
# Best practice, use a virtual environment rather than install in the base env
python -m venv c:\path\to\myenv
.\venv\Scripts\activate
# The actual install command
pip install numpy
```
* The repository already has some encoded texts to run as an example.
* The script should work with any encrypted text, as long as the cipher used to encrypt it was a simple substitution cipher, transposition cipher or substitution-plus-transposition product cipher.
