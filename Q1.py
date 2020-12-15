def CaesarEncrypt(text, shitNumber): 
    message = ""  
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            message += chr((ord(char) + shitNumber-65) % 26 + 65) 
        else: 
            message += chr((ord(char) + shitNumber - 97) % 26 + 97) 
    return message 
  
text = "OOOOJ"
s = 16
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Message: " + CaesarEncrypt(text,s))
