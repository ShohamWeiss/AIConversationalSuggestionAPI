from operator import truediv
from transformers import pipeline, AutoTokenizer
from Conversation import Conversation
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class Conversational():
    def __init__(self):
        self.model = pipeline('conversational', model='microsoft/DialoGPT-large', device=0 if torch.cuda.is_available() else -1)

    def generate_option(self, conversation:Conversation) -> str:        
        conv = conversation.to_huggingface_conversation()
        try:
            self.model(conv) 
        except:
            return ""
        return conv.generated_responses[-1]
    
if __name__=="__main__":
    
    conv = Conversation()
    conversational = Conversational()
    
    while(True):
        n = input("Input:")
        conv.add("Them", n)
        option = conversational.generate_option(conv)
        conv.add("Me", option)
        print(conv)
