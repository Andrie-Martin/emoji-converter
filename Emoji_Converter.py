# User message
message = input("> ")

# Track words in user's message
words = message.split(" ")

# Emoji Library
emoji = {
    ":)": "😊",
    ":(": "😟",
    "B)": "😎",
    "<3": "❤️"
}

output = ""
for word in words:
    output += emoji.get(word, word) + " "
print (output)
