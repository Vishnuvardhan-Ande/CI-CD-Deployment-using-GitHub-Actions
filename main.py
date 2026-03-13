from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD Deployment Successful"}

@app.get("/health")
def health_check():
    return  {"status": "healthy"}