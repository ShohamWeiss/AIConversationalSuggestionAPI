import torch
from transformers import pipeline

from Conversation import Conversation


class QA:
    def __init__(self):
        self.model = pipeline("question-answering", model="deepset/roberta-base-squad2",
                              device=0 if torch.cuda.is_available() else -1)

    def generate_options(self, conversation: Conversation, context: str) -> str:
        '''Generates options from a conversation by grabbing the last response and finding the answer in the context'''
        question = conversation.pop()
        # if context == "":
        if not context: return ""
        # run the model on the question and context
        # example: question = ["them","What is your name?", context = "My name is John"]
        result = self.model(question=question[1], context=context)
        # options = []
        # As the result is already sorted in descending, we have to choose the first one in any case
        return result[0]['answer']
        # check if result is a list
        # if not isinstance(result, list):
        #     return [result['answer']]
        # for multiple answers, return the first one with a score above 0.6
        # for option in result:
        #     if option["score"] > 0.6:
        #         options.append(option["answer"])
        # return options


# example for testing     
if __name__ == "__main__":
    conv = Conversation()
    qa = QA()

    while True:
        c = """Johny has two balloons, a blue and a red balloon.
            Johny fell down the stairs yesterday and broke his arm"""
        n = input("Question:")
        conv.add("Them", n)
        options = qa.generate_options(conv, c)
        print(options)
