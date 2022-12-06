class Token:
    def __init__(self,type,buffer,line,column):
        self.type = type
        self.buffer = buffer
        self.line = line
        self.column = column