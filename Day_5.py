# Practice Set 
# Q.1 Write a program to print Twinkle Twinkle Little Star poem :

#Solution:

print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.  ''')

 

# Q.2 print table of 5 

# Solution:
print("\n",5 * 1)
print("\n",5 * 2)
print("\n",5 * 3)
print("\n",5 * 4)
print("\n",5 * 5)
print("\n",5 * 6)
print("\n",5 * 7)
print("\n",5 * 8)
print("\n",5 * 9)
print("\n",5 * 10)\
    

# Q.3 install a External module and use is 

# Solution:
import pyttsx3
engine = pyttsx3.init()
engine.say(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.  ''')
engine.runAndWait()


# Q.4 Write a python program to print the content of a directory using the os module.
# Search online for the function which does that.

# Solution:
import os 
dir_path = '/'

content = os.listdir(dir_path)

for item in content:
    print(item)
    
    
    
    