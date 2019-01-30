import nltk
import ast
class Entity:
    # {'e_name':[values]}
    entities = {}
    # file_name = 'entities.json'
    def __init__(self,file_name='entities.txt'):
        self.Load(file_name)
    def Load(self,file_name):
        f = open(file_name,'r')
        try:
            self.entities = ast.literal_eval(f.read())
            f.close()
        except:
            print("Loding Error Entity")
    def Sys_ents(self,sent):
        pass
    def Extract(self,sent):
        extracted = []
        tokens = nltk.word_tokenize(sent)
        for tok in tokens:
            for ent in self.entities:
                if tok.lower() in self.entities[ent]:
                    extracted.append((ent,tok))

        return extracted
    def ByName(self,text,ent_name):
        tokens = nltk.word_tokenize(text)
        f=0
        for tok in tokens:
            if tok.lower() in self.entities[ent_name]:
                return (ent_name,tok)
                f=1

        if f==1:
            return None
