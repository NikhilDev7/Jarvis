import EntityEx
from Actions import *
from DataFile import *
class Analy:
    Class = None
    ents = None
    exit_flag = 0
    def __init__(self,Dict={}):
        if type(Dict)!=dict:
            print('Need a Dictonary')
        else:
            self.Class = Dict
    def IntentAnalysis(self,Dict):
        self.Class = Dict
        try:
            self.Start()
        except Exception as e:
            print("Error:"+e)
    def Start(self):
        self.Entity()
        if self.exit_flag==0:
            self.Contexts()
            print(self.Respose())
            self.Action()
        else:
            print("Canceled !!!!")
    def Entity(self):
        E = EntityEx.Entity()
        self.ents = E.Extract(self.Class['input']) # <-- [ ('ent_name','value'),.......]
        self.Requried()
    def Requried(self):
            for i in self.Class['entities']:
                # [{'n':'df'},{...}]
                f=0
                for j in self.ents:
                    # ('ent','val')
                    if i['name'] in j[0]:
                        f=1
                if f==0 and i['requried']:
                    print('Requried '+i['name'])
                    E = EntityEx.Entity()
                    while True:
                        e = input(i['prompt']+':')
                        if e.lower()=='cancel':
                            f=-1
                            self.exit_flag=1
                            break
                        t = E.ByName(e,i['name'])
                        if t !=None:
                            self.ents.append(t)
                            break
                if f==-1:
                    break
    def Action(self):
        # eg App.open('app_name')
        func_name = self.Class['action'][0] #eg App.open
        if func_name==None:
            return
        p = self.Class['action'][1]         #eg app_name
        # Gather the entities having name          ^
        if p!=None:
            para = ''
            for i in self.ents:
                if p in i[0]:
                    para=para+i[1]+','
            para=para[:-1]
            # print(func_name+"('"+para+"')")
            exec(func_name+"('"+para+"')")
        else:
            exec(func_name+"()")
    def Respose(self):
        if self.exit_flag==0:
            from random import choice
            return(choice(self.Class['responses']))
        else:
            return('No response')
    def Contexts(self):
        if self.Class['contexts'] != {}:
            I = Analy()
            I.IntentAnalysis(Data[self.Class['contexts']['output']])
            
