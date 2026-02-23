text = "" #<-Fnter your text here
binary_text = ' '.join(format(ord(c), '08b') for c in text)
print(binary_text) 