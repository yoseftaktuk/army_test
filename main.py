
from server.file_endler import file_endler1, get_file
from fastapi import FastAPI, UploadFile
import uvicorn
from make_base import make_base
app = FastAPI()

@app.get('/')
def home():
     home()

@app.post('/upload-csv')
def upload(file: UploadFile):
     get_file.upload_csv(file=file)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)


make_base.make_soldier()