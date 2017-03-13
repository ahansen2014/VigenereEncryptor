# VigenereEncryptor
A python app that encrypts data using the Vigenere cipher.  The app includes the function to read from and write to disk.

The app takes two inputs.  The first is the plain text in the upper text field.  This text can be mixed case and can contain alphanumeric characters as well as punctuation.  The punctuation is stripped prior to the encryption process.  Numbers are left in situ.  Note, this may lower the cipher security.

The output is a single string of characters all in upper case.  This is the encrypted data.
