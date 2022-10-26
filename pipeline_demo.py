'''
This file is a demo for the generational and conversational huggingface pipelines. The starter conversation is used to generate the first suggestions
which you can select by pressing 0,1,2,3 or 4. After each selection a new suggestion is made based on the enrire conversations history
'''

from Conversation import Conversation
from Conversational import Conversational
from Generator import Generator

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
conv.add("Them", "Why what happened?")
conv.add("Me", "I have a headache.")
conv.add("Them", "What do you think can help?")

print(conv)

conversational = Conversational()
gen = Generator()

while True:
    response = ""
    options = gen.generate_options(conv)
    options.append(conversational.generate_option(conv))
    options.append("TYPE")
    options.append("CLEAR")
    print(options)
    inp = int(input("Your choice: "))
    if inp == len(options) - 2:
        response += input("Your response: ")
        conv.pop()
    elif inp == len(options) - 1:
        response = ""
        conv.pop()
    else:
        response = f"Me:{options[inp]}"

    conv.add("Them", response)

    print(conv)
