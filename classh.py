class libro:
    def  __init__(self, titolo, anno, autore):
        self.titolo = titolo
        self.anno = anno
        self.autore = autore

    def get_titolo(self):
        return self.titolo

    def get_anno(self):
        return self.anno

    def get_autore(self):
        return self.autore

    def set_titolo(self, titolo):
        self.titolo = titolo

    def set_anno(self, anno):
        self.anno = anno

    def set_autore(self, autore):
        self.autore = autore

    def tostring(self):
        return "titolo: " + self.titolo + ", autore: "+ self.autore + ", anno: " + str(self.anno)

miolibro = libro("the kite runer", "2004", "david hayward")
print(miolibro.tostring())
print(miolibro.get_titolo())