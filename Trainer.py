import ast
class IntentManager():
    File = {}
    def Edit(self):
        pass
    def MakeIntent(self):
        #
        intent_name = input("Intent Name:")
        #
        contexts = {'input':[],'output':[]}
        temp = input('Enter Input Context:')
        if temp!="x":
            contexts['input'].append(temp)
        temp = input('Enter Output Context:')
        if temp!="x":
            contexts['output'].append(temp)
        #
        events = []
        while True:
            temp = input('Enter events_name:')
            if temp == "x":
                break
            events.append(temp)
        #
        action = []
        action_name = input('Enter Action_name:')
        if action_name!='x':
            action.append(action_name)
            para = input('Parameters(Seperated ,):')
            if para != 'x':
                action.append(para)
            else:
                action.append(None)
        else:
            action.append(None)
            action.append(None)
        #
        train_phares = []
        print("Training Phares:")
        while True:
            sample = input(">>")
            if sample == "x":
                break
            train_phares.append(sample)

        #
        entities = []
        while True:
            name = input('Entity Name:')
            if name =="x":
                break
            value = input('Value:')
            islist = input('islist yes/no:')
            requried = input('Requried yes/no')
            prompt = input('text')
            entities.append({'name':name,'value':value,'islist':islist,'requried':requried,'prompt':prompt})
        #
        responses = []
        print("Enter Responses")
        while True:
            res = input('>>')
            if res == "x":
                break
            responses.append(res)
        #
        Json = {}
        Json['contexts'] = contexts
        Json['events'] = events
        Json['train_phares'] = train_phares
        Json['action'] = action
        Json['entities'] = entities
        Json['responses'] = responses

        self.File = {intent_name:Json}
    def Save(self,path):
        #
        file = open(path,'a')
        file.write(str(self.File))
        file.close()
    def Load(self,path):
            try:
                file = open(path,'r')
                self.File  = ast.literal_eval(file.read())
                file.close()
            except:
                print('Loding error!!!')
    def Print(self):
        #
        print("Your Details")
        for i in self.File:
            print(i)
            print(self.File[i])

def main():
    I = IntentManager()
    I.Load('Data.json')
    I.MakeIntent()
    I.Print()
    I.Save('Data.json')

if __name__ == '__main__':
    main()
