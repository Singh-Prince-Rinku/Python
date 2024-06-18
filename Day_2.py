#python provide us the various or large amount of features that we can used to tackle any type
# of problem..
# In python, modules is just like packages where each module has different features and if you need 
# You can simply import but must be sure that packages are available in your python environment
# If there is no package available that you can install it using pip command like this:
# pip install pyjokes:
# pip install flask:

import pyjokes # I'm going to import pyjokes
jokes = pyjokes.get_joke() # then in pyjokes import pyjokes class that is get_jokes() and pass this into jokes variables
print(jokes) # Print the jokes thats it!