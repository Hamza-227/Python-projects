# IT WILL PRINT WHATEVER YOU WANT
import pyttsx3
engine = pyttsx3.init()
engine.say('''BONA''')
engine.runAndWait()

# IT WILL GIVE FOLDERS IN OS 
import os

# Select the directory whose content you want to list 
directory_path = '/Coding Things'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)