from fastapi import FastAPI
from pydantic import BaseModel
from model.manager import ModelManager

models = {}
app = FastAPI()

class FileData(BaseModel):
    model_name: str
    file_path: str
    target_name: str
    index_name: str

@app.put("/add_model")
def add_model(data: FileData):
    models[data.model_name] = ModelManager(data.file_path, data.index_name, data.target_name)
    return {
        "message": "Received data successfully.",
    }
@app.get("/get_models")
def get_models():
    return {
        "models": list(models.keys())
    }

@app.get("/make_test")
def make_test(model):
    score = models[model].test()
    return{
        "score": score
    }