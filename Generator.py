from copy import deepcopy

import torch
from transformers import pipeline, AutoTokenizer

from Conversation import Conversation


class Generator:
    def __init__(self):
        self.model = pipeline('text-generation', model='gpt2-large', device=0 if torch.cuda.is_available() else -1)
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2-large")

    def generate_options(self, conversation: Conversation, token_lengths=[1, 1, 2, 2]) -> list:
        '''Generates options from a conversation'''
        if not conversation: return []
        conversation_copy = deepcopy(conversation)
        '''Adding a me: to the end of the conversation to make sure the model doesn't generate a response to the last question
        [Me, Them, Me, Them] -> [Me, Them, Me, Them, Me]'''
        if conversation_copy.conversation[-1][0] != "me":
            conversation_copy.add("me", "")

        suggestions = []
        conv = str(conversation_copy)
        conv = conv[:-1]  # removing last \n to not confuse the model
        num_of_tokens = self.tokenizer(conv, return_tensors="pt").input_ids.shape[1]
        for token_length in token_lengths:
            # for each token length, generate a suggestion
            generated_text = self.model(
                conv,
                max_length=token_length + num_of_tokens,
                pad_token_id=self.tokenizer.eos_token_id  # to not get warning
            )
            # add the suggestion to the list (removing the input conversation from the generated text)
            suggestions.append(generated_text[0]['generated_text'].replace(f"{conv}", ""))

        return suggestions
