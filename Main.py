from LexicalAnalyzer import LexicalAnalyzer
file1 = open('Automata.afd',encoding='utf-8').read()
lexical = LexicalAnalyzer()
#print(file)
lexical.analyze(file1)
lexical.showTokens()
lexical.showErrors()