from urllib import response
from Conversation import Conversation
from Generator import Generator
from Conversational import Conversational
from transformers import Conversation as HuggingfaceConversation

# conv = Conversation()
# conv.add("John", "Hello")
# conv.add("Mary", "Hi")
# conv.add("John", "How are you?")
# conv.add("Mary", "")


conv = Conversation()
conv.add("Them", "Hello")
conv.add("Me", "Hi")
conv.add("Them", "How are you?")
conv.add("Me", "Not so good.")
conv.add("Them", "Why what happenned?")
conv.add("Me", "I have a headache.")
conv.add("Them", "What do you think can help?")

print(conv)

conversational = Conversational()
gen = Generator()

while(True):
    response = ""
    options = gen.generate_options(conv)
    options.append(conversational.generate_option(conv))
    options.append("TYPE")
    options.append("CLEAR")
    print(options)
    inp = int(input("Your choice: "))
    if (inp == len(options) - 2):
        response += input("Your response: ")
        conv.pop()
    elif (inp == len(options) - 1):
        response = ""
        conv.pop()
    else:
        response = f"Me:{options[inp]}"
        
    conv.add("Them", response)
    
    print(conv)