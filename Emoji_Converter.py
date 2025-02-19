# Emoji Library
emoji = {
    ":)": "😊",
    ":(": "😟",
    "B)": "😎",
    "<3": "❤️",
    ":D": "😃",
    ":P": "😛",
    ";)": "😉",
    ":O": "😲",
    "XD": "😂",
    ":/": "😕",
    ":|": "😐",
    "^-^": "😁",
    "T_T": "😭",
    "D:": "😨",
    "O_O": "😳",
    "-_-": "😑",
    "(:": "🙃",
    "<_<": "😒",
    ">_>": "😏",
    "*_*": "😍"
}

# User message
def emoji_converter(message):
    # Track words in user's message
    words = message.split(" ")

# Converter
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output
    
while True:
    message = input("> ")
    print (emoji_converter(message))
    continue