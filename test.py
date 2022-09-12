from urllib import response
from Conversation import Conversation
from Generator import Generator

conv = Conversation()
conv.add("John", "Hello")
conv.add("Mary", "Hi")
conv.add("John", "How are you?")
conv.add("Mary", "")

# conv = Conversation()
# conv.add("John", "Hello")
# conv.add("Mary", "Hi")
# conv.add("John", "How are you?")
# conv.add("Mary", "Not so good.")
# conv.add("John", "Why what happenned?")
# conv.add("Mary", "I have a headache.")
# conv.add("John", "What do you think can help?")
# conv.add("Mary", "")

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
        
    conv.add("Mary", response)
    
    print(conv.get_conversation_as_text()[:-1])
    