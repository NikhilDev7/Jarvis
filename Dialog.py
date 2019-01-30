from Intent import *
from ana import *
from timex import *

I = Intent()
I.Train()
class Dialog:
    sent = []
    dialogs = []
    Memory = []
    def DialogStart(self):
        while True:
            # User Inputs
            sentense = input('>>')
            if sentense in ['exit','q','bye']:
                break
            # Intent
            A = Analy()
            intent   = I.Predict(sentense,'dict')
            if intent!=[]:
                A.IntentAnalysis(intent)
                # Memory
                self.Memory.append(A.ents)
                # Store Dialogs
                self.dialogs.append((sentense,A.Respose()))
                # Content
            else:
                print('Can\'t get it')


def main():
    D = Dialog()
    D.DialogStart()
if __name__ == '__main__':
    main()
