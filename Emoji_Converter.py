# Emoji Library
emoji = {
    ":)": "😊",
    ":(": "😟",
    "B)": "😎",
    "<3": "❤️"
}

# User message
while True:
    message = input("> ")

# Track words in user's message
    words = message.split(" ")

# Converter
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    print (output)
    continue