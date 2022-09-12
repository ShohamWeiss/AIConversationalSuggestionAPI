from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/suggest_next_word")
async def suggest_next_word(suggestion_sizes: list, context: list[list]):
    ''' Code to generate suggestions using Generative model '''
    
    # Parse Context to Conversation object
    # Run Generative model on Conversation object
    # Convert Suggestions to JSON
    return {f"{context}"}

@app.post("/suggest_from_response")
async def suggest_from_response(num_of_answers: list, context: list[list], aboutme: str):
    ''' Code to generate suggestions using Generative, Conversational, and QA model '''
    
    # Parse Context to Conversation object
    # Run QA model on last Conversation object with aboutme    
    return {f"{context}"}

if __name__ == "__main__":
    uvicorn.run(app)