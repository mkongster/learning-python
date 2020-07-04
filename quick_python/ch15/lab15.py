class html:
    def __init__(self, subelement=None):
        self.subelement = subelement
    
    def __str__(self):
        print('<html>')
        print(self.subelement)
        return '</html>'


class subelement:
    def __init__(self, text):
        self.text = text


class body(subelement):
    def __init__(self, text=None, subelement=None):
        super().__init__(text)
        self.subelement = subelement
    
    def __str__(self):
        print('<' + body.__name__ + '>')
        print(self.text)
        print(self.subelement)
        return '</' + body.__name__ + '>'
    

class p(subelement):
    def __init__(self, text):
        super().__init__(text)

    def __str__(self):
        print('<' + p.__name__ + '>')
        print(self.text)
        return '</' + p.__name__ + '>'

def main():
    para = p(text='this is some body text')
    doc_body = body(text='This is the body', subelement=para)
    doc = html(subelement=doc_body)
    print(doc)


if __name__ == '__main__':
    main()