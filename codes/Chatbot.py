import nltk
from nltk.chat.util import Chat, reflections

# chatbot questions and answers
pairs = [

    [r"hi|hello|hey",
     ["Hello! Welcome to Ice Cream Shop "]],

    [r"flavor ?",
     ["We have chocolate, vanilla and strawberry."]],

    [r"price",
     ["Ice cream starts from 50 rupees."]],

    [r"timing",
     ["Shop is open from 10 AM to 11 PM."]],

    [r"bye",
     ["Bye! Visit again "]]
]

# create chatbot
chatbot = Chat(pairs, reflections)

print("Ice Cream Shop Chatbot")
print("Type 'bye' to exit\n")

# start chat
chatbot.converse()