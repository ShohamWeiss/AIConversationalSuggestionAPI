from transformers import pipeline, AutoTokenizer
from Conversation import Conversation

class Generator():
    def __init__(self, token_lengths = [1,1,2,2]):
        self.model = pipeline('text-generation', model = 'gpt2-large')        
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2-large")
        self.token_lengths = token_lengths    

    def generate_options(self, conversation):
        suggestions = []
        conv = conversation.get_conversation_as_text()
        conv = conv[:-1]
        num_of_tokens = self.tokenizer(conv, return_tensors="pt").input_ids.shape[1]
        for token_length in self.token_lengths:
            generated_text = self.model(
                conv,
                max_length = token_length+num_of_tokens,
                pad_token_id=self.tokenizer.eos_token_id
            )            
            suggestions.append(generated_text[0]['generated_text'].replace(f"{conv}", ""))
            
        return suggestions