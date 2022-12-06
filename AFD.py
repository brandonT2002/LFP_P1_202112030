class AFD:
    def __init__(self,automatonName,states,alphabet,initialState,acceptingStates,transitions):
        self.name = automatonName
        self.states = states
        self.alphabet = alphabet
        self.initialState = initialState
        self.acceptingStates = acceptingStates
        self.transitions = transitions