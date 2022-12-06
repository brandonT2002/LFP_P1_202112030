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