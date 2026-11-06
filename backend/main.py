from fastapi import FastAPI

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