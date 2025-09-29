import pyttsx3
import os


# Q-1) print simple twinkle twinkle poem

poem  = "Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.When the blazing sun is set, and the grass with dew is wet. Then you show your little light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you are. Then the traveler in the dark thanks you for your tiny spark. How could he see where togo if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are. As your bright and tiny spark lights the traveler in the dark, though I know not what you are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are"

print(
    '''
Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.

Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are
'''
)


# print(poem)


# Q-2) print table of five
a = 5
for b in range(1,11):
               print(a * b)


#Q-3) use pip install to intall any external module or package:
engine = pyttsx3.init()
engine.say("Ahmed Yar, how are you ? ")
engine.runAndWait()



#Q-4) write a print each file in your directory
directory_path = "/Ahmed"

content = os.listdir(directory_path)

for items in content:
        print(items)


        
#Q-5) label the things in comment

# our first comment 
# our second comment 
# our third comment 