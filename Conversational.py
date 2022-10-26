import torch
from transformers import pipeline

from Conversation import Conversation


class Conversational:
    def __init__(self):
        self.model = pipeline('conversational', model='microsoft/DialoGPT-large',
                              device=0 if torch.cuda.is_available() else -1)

    def generate_option(self, conversation: Conversation) -> str:
        # Convert to huggingface Conversation
        conv = conversation.to_huggingface_conversation()
        try:
            # Call model with conversation
            self.model(conv)
        except:
            return ""
        # Get last response
        return conv.generated_responses[-1]


if __name__ == "__main__":

    conv = Conversation()
    conversational = Conversational()

    while True:
        n = input("Input:")
        conv.add("Them", n)
        option = conversational.generate_option(conv)
        conv.add("Me", option)
        print(conv)
