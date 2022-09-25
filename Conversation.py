from transformers import Conversation as HuggingfaceConversation

class Conversation():
    def __init__(self, hf_conversation:HuggingfaceConversation=None):
        self.conversation = []
        if hf_conversation is not None:
            self.from_huggingface_conversation(hf_conversation)
    
    def __init__(self, conversation_list:list[list]=None):
        self.conversation = []
        if conversation_list is not None:
            self.from_list_of_list(conversation_list)
            
    def add(self, paticipant, message):
        self.conversation.append([paticipant, message])

    def __str__(self) -> str:
        text = ""
        for message in self.conversation:
            text += message[0] + ":" + message[1] + "\n"
        return text        
    
    def pop(self):
        return self.conversation.pop(-1)
    
    def from_list_of_list(self, conversation_list:list[list]):
        for message in conversation_list:
            self.add(message[0], message[1])
    
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