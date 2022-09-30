from urllib import response
from fastapi import FastAPI
import uvicorn
from Conversation import Conversation
from Generator import Generator
from Conversational import Conversational
from QA import QA
import json
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
# allow cross origin requests
origins = [    
    "http://localhost",
    "http://localhost:8080",
    "file://"    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SuggestFromResponseModel(BaseModel):
    conversation: list[list]
    aboutme: str    

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
    return suggestions

@app.post("/suggest_from_response")
async def suggest_from_response(request: SuggestFromResponseModel):
    ''' Generate suggestions using Generative, Conversational, and QA model '''
    
    # Parse Context to Conversation object
    conversation = Conversation(conversation_list=request.conversation)
    # Run Generative model on Conversation object
    gen_suggestions = generative_model.generate_options(conversation, [1,1,2,2,4])
    # Run Conversational model on Conversation object
    conv_suggestions = conversational_model.generate_option(conversation)
    # Run QA model on last Conversation object with aboutme
    qa_suggestions = qa_model.generate_options(conversation, request.aboutme)
    # Combine suggestions        
    suggestions = { "gen": gen_suggestions, "conv": conv_suggestions, "qa": qa_suggestions }
    return suggestions

if __name__ == "__main__":
    print("loading generative model")
    generative_model = Generator()    
    print("loading conversational model")
    conversational_model = Conversational()
    print("loading QA model")
    qa_model = QA()
    print("starting server")
    uvicorn.run(app)