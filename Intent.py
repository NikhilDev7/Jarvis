import nltk
from nltk.stem.lancaster import LancasterStemmer
# from info import *
Stemmer = LancasterStemmer()
import ast
class Intent:
    Data = {}
    Class_words = {}
    def __init__(self,file_path='Data.json'):
        f = open(file_path,'r')
        try:
            self.Data = ast.literal_eval(f.read())
            f.close()
            print(self.Data)
        except:
            print("Loding Error Intent")
    def Train(self):
        Intent_data = {}
        # Get all names and their train_phares
        for c in self.Data:
            Intent_data[c]=self.Data[c]['train_phares']
            self.Class_words[c]=[]
        # # Creates name and words relatedto it
        corpus_word = {}
        for data in Intent_data:
                # Tokenize each sent in words
                for phares in Intent_data[data]:
                    for word in nltk.word_tokenize(phares):
                        if word not in ['?',"'s'",'{','}']:
                            # Stem and lower words
                            stem_word = Stemmer.stem(word.lower())
                            if stem_word not in corpus_word:
                                corpus_word[stem_word] = 1
                            else:
                                corpus_word[stem_word] += 1
                        #  Add words to class list
                        if stem_word not in self.Class_words[data]:
                            self.Class_words[data].append(stem_word)
    def Print(self):
        for i in self.Class_words:
            print(i)
            print(self.Class_words[i])
    def cal_score(self,sent,class_name,show=False):
        score = 0
        for i in nltk.word_tokenize(sent):
            if Stemmer.stem(i.lower()) in self.Class_words[class_name]:
                score+=1
                if show==True:
                    print(class_name+' : '+i)
        return score
    def score_analysis(self,List):
        l = List[:]


        # Prompts to select one Intent
        print('What u want to do?')
        for i in range(len(List)):
            print('{}.{}'.format(i+1,List[i]))
            List[i]=List[i].lower()
        sent = input('>>?').lower()
        if sent in List:
            return l[List.index(sent)]
        return None

    def Predict(self,text,return_type='text'):
        cl = None
        same_score=[]
        score=self.cal_score(text,list(self.Class_words.keys())[0])
        # Iterate Over Class words and get scores
        for i in self.Class_words:
            s = self.cal_score(text,i)
            if score < s:
                same_score.clear()
                cl=i
            elif score==s:
                if s!=0:
                    same_score.append(i)
            score=s
        # if Classes have same score select one
        if same_score!=[]:
            # Entity Score
            import EntityEx
            E =EntityEx.Entity()
            score = 0
            for i in self.Class_words:
                for j in self.Data[i]['entities']:
                        score=E.ByName(text,j['name'])
                        if score!=None:
                            cl=i
                            break
                if score!=None:
                    break
            # Prompt Method
            if score==None:
                cl = self.score_analysis(same_score)
        if return_type=='text':
            if cl==None:
                return []
            else:
                return cl
        if return_type=='dict':
            if cl in self.Data:
                self.Data[cl]['input']=text
                return self.Data[cl]
            else:
                return []




def main():
    pass
    # I = IntentManager()
    # I.Load('Jdata.json')
    # I.Print()
    # C = Intent()
    # C.Train(I.File)
    # # C.Print()
    # print(C.Predict('Launch Open'))

if __name__ == '__main__':
    main()
