from fastapi import FastAPI
import uvicorn

klu = FastAPI(
    title="AI tutor",
    description="Ai tutor PBL Project",
    version="1.0.0",
)

@klu.get("/")
def home():
    return {"message": "welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message": "KL University"}

@klu.get("/ask")
def ask():
    return {"message": "what is LLM", "answer": "Large Language Model"}

@klu.get("/student")
def student():
    return{"id": 1, "name": "Ram", "gender": "male", "course": "DSA"}

@klu.get("/students")
def students():
    return [{"id": 1, "name": "Ram", "gender": "male", "course": "DSA"},
         {"id": 2, "name": "Shyam", "gender": "male", "course": "DSA"},
         {"id": 3, "name": "Sita", "gender": "female", "course": "DSA"}]

if __name__ == "__main__":
    uvicorn.run("main:klu",host="127.0.0.1",port=2027,reload=True)

    