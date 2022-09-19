from transformers import Conversation as HuggingfaceConversation

class Conversation():
    def __init__(self, conversation:HuggingfaceConversation=None):
        self.conversation = []
        if conversation is not None:
            self.from_huggingface_conversation(conversation)
            
    def add(self, paticipant, message):
        self.conversation.append([paticipant, message])

    def __str__(self) -> str:
        text = ""
        for message in self.conversation:
            text += message[0] + ":" + message[1] + "\n"
        return text        
    
    def pop(self):
        return self.conversation.pop(-1)
    
    def from_huggingface_conversation(self, conversation):
        for message in conversation.iter_texts():
            participant = "them"
            if (message[0]):
                participant = "me"
            self.add(participant, message[1])
            
    def to_huggingface_conversation(self) -> HuggingfaceConversation:
        hf_conv = HuggingfaceConversation()
        for message in self.conversation:
            if (message[0].lower() == "them"):
                hf_conv.add_user_input(message[1])
            else:
                hf_conv.append_response(message[1])
                hf_conv.mark_processed()
        return hf_conv