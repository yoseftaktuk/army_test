import json

file_path = 'C:\\Users\\Yosef\\PycharmProjects\\army_test\\data\\data.json'

def load_data():
    with open(file_path,'r+',encoding="utf-8") as f:
         return json.load(f)
    
    
def seve_data(data):
    with open(file_path,'w',encoding="utf-8") as f:
        json.dump(data,f)    
