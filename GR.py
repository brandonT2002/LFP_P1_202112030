class GR:
    def __init__(self,grammarName,nonTerminal,terminals,initialNonTerminal,rules):
        self.grammarName = grammarName
        self.nonTerminal = nonTerminal
        self.terminals = terminals
        self.initialNonTerminal = initialNonTerminal
        self.rules = rules