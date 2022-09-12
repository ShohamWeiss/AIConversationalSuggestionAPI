from fastapi import FastAPI, File
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/suggest_next_word")
async def suggest_next_word(suggestion_sizes: list, context: list[list]):
    ''' Code to generate suggestions using Generative model and Conversation model '''
    
    # Parse Context to Conversation object
    # Run Generative model on Conversation object
    return {f"{context}"}

@app.post("/suggest_from_qa")
async def suggest_from_qa(num_of_answers: list, context: list[list], aboutme: str):
    ''' Code to generate suggestions using QA model '''
    
    # Parse Context to Conversation object
    # Run QA model on last Conversation object with aboutme    
    return {f"{context}"}

if __name__ == "__main__":
    uvicorn.run(app)