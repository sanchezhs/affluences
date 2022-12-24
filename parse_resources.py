import re

class ParserException(Exception): pass
class Parser:

    def __init__(self, file):
        self.numbers = []
        self.token_pattern = r"""
        (?P<ident>resource_id.{1,10}[0-9]+)
        |(?P<name>resource_name.{1,50}[0-9]+)
        #|(?P<identifier>[a-zA-Z_][a-zA-Z0-9_]*)
        #|(?P<integer>[0-9]+)
        |(?P<basura>.)
        """
        self.text = file

    def add(self, tok):
        self.numbers.append(tok)

    def print_numbers(self):
        print(self.numbers)

    def tokenize(self):
        token_re = re.compile(self.token_pattern, re.VERBOSE)
        pos = 0
        while True:
            m = token_re.match(self.text, pos)
            if not m: break
            pos = m.end()
            tokname = m.lastgroup
            tokvalue = m.group(tokname)
            yield tokname, tokvalue
        if pos != len(self.text):
            raise ParserException('tokenizer stopped at pos %r of %r' % (
                pos, len(self.text)))
   
    def to_list(self):
        number_pattern = '[0-9]+'
        number_re = re.compile(number_pattern)
        for token in self.tokenize():
            if 'basura' not in token:
                self.add(re.search(number_pattern, str(token)).group(0))
        return self.numbers
    

