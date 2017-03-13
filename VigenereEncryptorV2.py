from Tkinter import *
from tkFileDialog import askopenfilename, asksaveasfilename

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

punctuation = [',','.',':',' ','?','!','\n']

vigenere = {
    'A' : ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
    'B' : ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
    'C' : ['C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B'],
    'D' : ['D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C'],
    'E' : ['E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D'],
    'F' : ['F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E'],
    'G' : ['G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F'],
    'H' : ['H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G'],
    'I' : ['I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H'],
    'J' : ['J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I'],
    'K' : ['K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J'],
    'L' : ['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K'],
    'M' : ['M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L'],
    'N' : ['N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M'],
    'O' : ['O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N'],
    'P' : ['P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'],
    'Q' : ['Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'],
    'R' : ['R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q'],
    'S' : ['S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'],
    'T' : ['T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S'],
    'U' : ['U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'],
    'V' : ['V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'],
    'W' : ['W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V'],
    'X' : ['X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'],
    'Y' : ['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'],
    'Z' : ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']
    }

def load_button_handler():
    '''
    This is a simple function to read the contents of a text file
    and display them in a text widget.
    :return: Nothing is returned.
    '''
    try:
        filePath = askopenfilename()
        with open(filePath,'r') as file:
            plainTextStr = file.read()
            txtPlainText.insert(0.0,plainTextStr)
    except:
        print('The user cancelled.')

def code_button_handler():
    '''
    This is the encryption routine.  Two strings are needed, the input string and the keyword.
    The input string is stripped of punctuation (this needs updating as it does not include all
    punctuation) and converted to upper case.  The keyword is converted to upper case as well.

    Any numbers are left in situ, which may weaken the encryption, and the reamining characters
    are encrypted acording to the vigenere dictionary.

    The final string is displayed in the lower text field.
    :return: Encrypted string.
    '''
    inputText = txtPlainText.get(0.0,END)
    keyword = txtKeyword.get().upper()

    for item in punctuation:
        inputText = inputText.replace(item, '')
    inputText = inputText.upper()

    # Now, do the encryption
    cipherString = ''
    keypointer = 0
    for character in inputText:
        if character in numbers:
            cipherString = cipherString + character

        elif character in alphabet:
            plainIndex = alphabet.index(character)
            keyLetter = keyword[keypointer]
            cipherString = cipherString + vigenere[keyLetter][plainIndex]
            keypointer += 1
            if keypointer == len(keyword):
                keypointer = 0

    txtCipherText.delete(0.0, END)
    txtCipherText.insert(0.0, cipherString)


def save_button_handler():
    '''
    This is a simple function to write the contents of a text file.
    :return: Nothing is returned.
    '''
    try:
        filePath = asksaveasfilename()
        with open(filePath,'w') as file:
            file.write(txtCipherText.get(0.0, END))
    except:
        print('The user cancelled.')



main = Tk()
main.geometry('600x500')
main.title('Vigenere Cipher Encryptor v2.0')

lbSpace1 = Label(main, text='     ').grid(row=0, column=0)

txtPlainText = Text(main, width=75, height=12, bd=10)
txtPlainText.grid(row=1, column=1, columnspan=5)
txtPlainText.config(wrap=WORD)
txtPlainText.focus_set()

lbKeyword = Label(main, text='Keyword').grid(row=2, column=1)

txtKeyword = Entry(main)
txtKeyword.grid(row=2, column=2)

pbLoad = Button(main, text='Load', command=load_button_handler)
pbLoad.grid(row=2, column=3)

pbRotate = Button(main, text='Encrypt', command=code_button_handler)
pbRotate.grid(row=2, column=4)

pbSave = Button(main, text='Save', command=save_button_handler)
pbSave.grid(row=2, column=5)

txtCipherText = Text(main, width=75, height=12)
txtCipherText.grid(row=3, column=1, columnspan=5)
txtCipherText.config(wrap=WORD)

mainloop()