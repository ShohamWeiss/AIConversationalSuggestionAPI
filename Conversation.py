class Conversation():
    def __init__(self):
        self.conversation = []
    
    def add_(self, paticipant, message):
        self.conversation.append([paticipant, message])

    def get_conversation_as_text(self):
        text = ""
        for message in self.conversation:
            text += message[0] + ":" + message[1] + "\n"
        return text        
    
    def pop(self):
        return self.conversation.pop(-1)