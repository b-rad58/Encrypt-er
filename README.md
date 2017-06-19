# Encrypt-er

encrypter.py

A script that will perform the encryption stage of a Vigenère cipher. The
script takes in as input three arguments. The first is the name of the
file to be encrypted, the second is the encryption key and the third is a name of
the file the encrypted text will be written to. The script does not encrypt
numbers and removes all non-letter and non-number characters, this
includes newline characters (there should be no newline characters in the
encrypted file). E.g a 3 will stay a 3 and a ‘.‘ would not be added to the
encrypted file. All encrypted letters will be in upper case.

decrypter.py

The same as encrypter.py but doing the decryption stage of a Vigenère cipher
instead. Opposite of encrypter.py, going from a coded message
to a decoded message using similar arguments.
