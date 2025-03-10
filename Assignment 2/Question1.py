from flask import Flask

app = Flask(__name__)

def processor(name: str) -> str:
    
    name = name.strip()
    new_name = ''

    if name.isupper():
        return name.lower()
    
    elif name.islower():
        return name.upper()
    
    elif not name.isalpha():
        for char in name:
            if char.isalpha():
                new_name += char
        return new_name.upper()
    
    else:
        return name.title()
    
def palindrome_detector(name: str) -> bool:

    length = len(name)

    for i in range(length // 2):
        if name[i] != name[length - i- 1]:
            return False
    return True

def emoji_converter(name: str) -> str:
    
    new_name = ''

    for char in name:
        if char == 'A' or char == 'a':
            new_name += '🔺'
        elif char == 'E' or char == 'e':
            new_name += '🎗'
        elif char == 'I' or char == 'i':
            new_name += '👁'
        elif char == 'O' or char == 'o':
            new_name += '🔵'
        elif char == 'U' or char == 'u':
            new_name += '🆙'
        else:
            new_name += char

    return new_name
    
@app.route("/<user_name>")
def web_response(user_name):

    name = processor(user_name)

    if palindrome_detector(name):
        return "Welcome, " + name + ". Your name is a palindrome!"
    
    return "Welcome, " + name + ", to my CSCB20 website!"

@app.route("/emoji/<new_name>")
def emoji_name_response(new_name):

    name = emoji_converter(new_name)

    return "Welcome, " + name + ", to my CSCB20 website!"

if __name__ == "__main__":
    app.run(debug=True)