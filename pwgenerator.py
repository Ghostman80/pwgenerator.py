import random

# Function to shuffle all the characters.
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return '' .join(tempList)

#Main program starts here
lowercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter3=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter4=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter5=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter6=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter7=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter8=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
#...

#Generate password using all the characters, in random order. 
password = lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + lowercaseLetter6 + lowercaseLetter7 + lowercaseLetter8 # + ....
password = shuffle(password)

#Output
print(password)

input ("Thank you!")