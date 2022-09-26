from urllib import response
from fastapi import FastAPI
import uvicorn
from Conversation import Conversation
from Generator import Generator
from Conversational import Conversational
from QA import QA
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/suggest_next_word")
async def suggest_next_word(conversation: list[list], suggestion_sizes: list = [1,1,2,2,4]):
    ''' Generate suggestions using Generative model '''
        
    # Parse Context to Conversation object
    conversation = Conversation(conversation_list=conversation)
    # Run Generative model on Conversation object
    suggestions = generative_model.generate_options(conversation, suggestion_sizes)
    # Convert Suggestions to JSON
    response = json.dumps(suggestions)
    return response

@app.post("/suggest_from_response")
async def suggest_from_response(conversation: list[list], aboutme: str, num_of_answers: list):
    ''' Generate suggestions using Generative, Conversational, and QA model '''
    
    # Parse Context to Conversation object
    conversation = Conversation(conversation_list=conversation)
    # Run Generative model on Conversation object
    gen_suggestions = generative_model.generate_options(conversation, [1,1,2,2,4])
    # Run Conversational model on Conversation object
    conv_suggestions = conversational_model.generate_option(conversation)
    # Run QA model on last Conversation object with aboutme
    qa_suggestions = qa_model.generate_options(conversation, aboutme)
    # Convert Suggestions to JSON
    suggestions = { "gen": gen_suggestions, "conv": conv_suggestions, "qa": qa_suggestions }
    response = json.dumps(suggestions)
    return response

if __name__ == "__main__":
    print("loading generative model")
    generative_model = Generator()    
    print("loading conversational model")
    conversational_model = Conversational()
    print("loading QA model")
    qa_model = QA()
    print("starting server")
    uvicorn.run(app)