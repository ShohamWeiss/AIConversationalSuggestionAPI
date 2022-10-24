from operator import truediv
import re
from transformers import pipeline, AutoTokenizer
from Conversation import Conversation
import torch

class QA():
    def __init__(self):
        self.model = pipeline("question-answering", model="deepset/roberta-base-squad2", device=0 if torch.cuda.is_available() else -1)
        
    def generate_options(self, conversation:Conversation, context:str) -> str:
        '''Generates options from a conversation'''  
        question = conversation.pop()
        if (context == ""):
            return ""
        result = self.model(question=question[1], context=context)
        options = []
        # check if result is a list
        if (not isinstance(result, list)):
            return [result['answer']]
                              
        for option in result:
            if option["score"] > 0.6:
                options.append(option["answer"])
        
        return options
    
# example for testing     
if __name__=="__main__":
    conv = Conversation()    
    qa = QA()
    
    while(True):
        c = """Jhonny has two balloons, a blue and a red balloon.
            Jhonny fell down the stairs yesterday and broke his arm"""
        n = input("Question:")
        conv.add("Them", n)
        options = qa.generate_options(conv, c)
        print(options)
