from Intent import *
from ana import *
from timex import *
# Take input
# sent = input('>>')

# Clasify Intent
I = Intent()
I.Train()
while True:
    sent = input('>>')
    d = I.Predict(sent,'dict')
    # Analysis
    if d!=[]:
        A = Analy(d)
        A.Start()
    else:
        print('Sorry i can\'t get it')
        print('Can you say again')
# Findall(sent)
# res = tag(sent)
