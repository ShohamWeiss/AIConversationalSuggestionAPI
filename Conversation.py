from transformers import Conversation as HuggingfaceConversation

class Conversation():
    ''' Contains a list of list of strings. example: [["them", "Hello"], ["me", "Hi"]] '''
    
    def __init__(self, hf_conversation:HuggingfaceConversation=None):
        ''' Create a Conversation object from a Huggingface Conversation object ''' 
        self.conversation = []
        if hf_conversation is not None:
            self.from_huggingface_conversation(hf_conversation)
    
    def __init__(self, conversation_list:list[list]=None):
        ''' Create a Conversation object from a list of lists '''
        self.conversation = []
        if conversation_list is not None:
            self.from_list_of_list(conversation_list)
            
    def add(self, paticipant, message):
        ''' Add a message to the conversation '''
        self.conversation.append([paticipant, message])

    def __len__(self):
        return len(self.conversation)
    
    def __str__(self) -> str:
        text = ""
        for message in self.conversation:
            # example: "Them: Hello"
            text += message[0] + ":" + message[1] + "\n"
        return text
    
    def pop(self):
        ''' Remove the last message from the conversation '''
        return self.conversation.pop(-1)
    
    def from_list_of_list(self, conversation_list:list[list]):
        ''' Helper function for creating a Conversation object from a list of lists '''
        for message in conversation_list:
            self.add(message[0], message[1])
    
    def from_huggingface_conversation(self, conversation):
        ''' Helper function for creating a Conversation object from a Huggingface Conversation object '''
        for message in conversation.iter_texts():
            participant = "them"
            if (message[0]):
                participant = "me"
            self.add(participant, message[1])
            
    def to_huggingface_conversation(self) -> HuggingfaceConversation:
        ''' Helper function for creating a Huggingface Conversation object from a Conversation object '''
        hf_conv = HuggingfaceConversation()
        for message in self.conversation:
            if (message[0].lower() == "them"):
                # example: "them: Hello"
                hf_conv.add_user_input(message[1])
            else:
                # example: "me: Hello"
                hf_conv.append_response(message[1])
                hf_conv.mark_processed()
        return hf_conv