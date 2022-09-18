class Rule():
    def __init__(self, term_left, term_right):
        self.left = term_left
        self.right = term_right
    
    def __str__(self):
        return f'{self.left} -> {self.right}'

    def __eq__(self, o):
        return str(self) == str(o)

    def __hash__(self):
        return len(str(self))