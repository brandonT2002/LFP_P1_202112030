from Error import Error
from Token import Token
from prettytable import Prettytable

class LexicalAnalyzer:
    def __init__(self):
        self.tokens = []
        self.errors = []
        self.line = 1
        self.column = 1
        self.status = 0
        self.buffer = ''

    def addError(self,character):
        self.errors.append(Error(f'caracter sin reconocer - {character}',self.line,self.column))
        self.status = 0
        self.column += 1
        self.buffer += ''

    def addToken(self,type,buffer):
        self.tokens.append(Token(type,buffer,self.line,self.column))
        self.i -= 1
        self.buffer = ''
        self.status = 0

    def showErrors(self):
        print('\nERRORS')
        x = Prettytable()
        x.field_names = ['Description','Line','Column']
        for error in self.errors:
            x.add_row([error.character,error.line,error.column])
        print(x)

    def showTokens(self):
        print('\nTOKENS')
        x = Prettytable()
        x.field_names = ['Token','Type','Line','Column']

    def s0(self,character):
        if character.isalpha():
            self.status = 1
            self.column += 1
            self.buffer += character
        elif character == ',':
            self.status = 2
            self.column += 1
            self.buffer += character
        elif character == ';':
            self.status = 3
            self.column += 1
            self.buffer += character
        elif character == '%':
            self.status = 4
            self.column += 1
            self.buffer += character
        elif character == '$':
            self.status = 5
            self.column += 1
            self.buffer += character
        elif character == '|':
            self.status = 6
            self.column += 1
            self.buffer += character
        elif character.isdigit():
            self.status = 7
            self.column += 1
            self.buffer += character
        elif character in [' ']:
            self.column += 1
        elif character == '\n':
            self.line += 1
            self.column += 1
        elif character == '#':
            pass
        else:
            self.addError(character)

    def s1(self,character):
        if character.isalpha() or character.isdigit() or character in ['-','_']:
            self.status = 1
            self.column += 1
            self.buffer += character
        else:
            self.addToken('string',self.buffer)

    def s2(self):
        self.addToken('comma',self.buffer)
    
    def s3(self):
        self.addToken('semicolon',self.buffer)

    def s4(self):
        self.addToken('percentage',self.buffer)

    def s5(self):
        self.addToken('dollar',self.buffer)

    def s6(self):
        self.addToken('or',self.buffer)

    def s7(self,character):
        if character.isdigit():
            self.status = 7
            self.column += 1
            self.buffer += character
        else:
            self.addToken('number',self.buffer)