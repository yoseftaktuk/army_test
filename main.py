
from server.file_endler import file_endler1, get_file
from fastapi import FastAPI, UploadFile
import uvicorn
from make_base import make_base
from server import logic
import json
num_residences = 2
app = FastAPI()

@app.get('/')
def home():
     home()

@app.post('/upload-csv')
def upload(file: UploadFile):
     get_file.upload_csv(file=file)
     

@app.post('/placement')
def placement():
     #data = file_endler1.load_data()
     data = make_base.make_base(num_residences)
     data1 = logic.get_info(data)
     info = logic.checking_every_soldier(data=data)
     print(info)
     return{'Registration was successful.\n'
     'Number of registered soldiers \n',{data1[0]},
     'Number of unregistered soldiers\n',{data1[1]}
     ,'\n',json.dump.items}
     
@app.get('/soldier_registration')
def get_soldier_registration():
    data = file_endler1.load_data()
    return data

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)



