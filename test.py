from urllib import response
from Conversation import Conversation
from Generator import Generator

conv = Conversation()
conv.add_("John", "Hello")
conv.add_("Mary", "Hi")
conv.add_("John", "How are you?")
conv.add_("Mary", "")

conv = Conversation()
conv.add_("John", "Hello")
conv.add_("Mary", "Hi")
conv.add_("John", "How are you?")
conv.add_("Mary", "Not so good.")
conv.add_("John", "Why what happenned?")
conv.add_("Mary", "I have a headache.")
conv.add_("John", "What do you think can help?")
conv.add_("Mary", "")

print(conv.get_conversation_as_text()[:-1])

gen = Generator()
while(True):
    response = ""
    options = gen.generate_options(conv)
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
        response = conv.pop()[1]
        response += options[inp]
        
    conv.add_("Mary", response)
    
    print(conv.get_conversation_as_text()[:-1])
    