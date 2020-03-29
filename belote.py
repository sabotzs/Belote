class Belote:
    def __init__(self, pair):
        self.pair = pair

    def __eq__(self, other):
    	return self.pair == other.pair

    def __int__(self):
        return 20

    def __repr__(self):
        return 'belote'