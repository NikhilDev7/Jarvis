import ast

f = open('Data.json','r')
try:
    Data = ast.literal_eval(f.read())
except Exception as err:
    print("Error Data "+err)
        
