class Term():
    def __init__(self, term_type=None, content=None, name=None):
        """
        term_type = 'var' | 'constructor'
        """

        if term_type not in ['var', 'constructor']:
            raise Exception('неверный параметр при создании терма')

        self.type = term_type
        self.name = name
        self.content = content

    def __str__(self):
        if self.type =='constructor':
            x = list(map(str, self.content))
            return f'{self.name}({",".join(x)})'
        
        return str(self.name)

    def string_representation(self):
        return str(self)

    def __eq__(self, o):
        return str(self) == str(o)

    def __ne__(self, o):
        return str(self) != str(o)
