#Day 6

'''
print('MY LOGIN SYSTEM')
print('---------------')

username = input('Username > ')
password = input('Password > ')

if username == 'Tom' and password == 'myspace99':
  print('Hello there Tom! You made quite a great social network back in the day. Too bad it went downhill from there.')
elif username == 'Jamie' and password == 'lannister69':
  print('Hello there Jamie! You better hurry up and go see your sister before you dad gets home')
elif username == 'Mchief' and password == 'iluvcortana':
  print('Halo there Masterchief! Have a great day killing those Covenant scum.')
else:
  print('Go away!')

'''


'''

season = input("what is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")


'''


'''

print('SECURE LOGIN')
username = input('Username > ')
password = input('Password > ')

if username == "Frank" and password == 'password1':
  print('Hello Frank!')
elif username == "Chiara" and password == 'Ch1ara88':
  print('Hello Chiara!')
else:
  print('Go away!')
  

'''




#Day 5

'''

print("=== Game of Thrones Character Creator ===")
print()
q1 = input("Do you like to the thick of the battle? ")
if q1 == "yes":
  print("You are a Stark!")
else:
  print("You are a Lannister.")

'''

'''
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")
'''

'''
myName = input("What's your name?: ")
if myName == "Frank":
  print("Yo what's up bro?")
else:
  print("Where's Frank?")

'''



#Day 4

'''
print("=== Your Adventure Simulator ===")
print("""You'll be asked a bunch of questions thn we'll make you up an amazing story with YOU as the star! 🤩""")
print()
name = input("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input("Your super power: ")
fear = input("Your biggest fear: ")
location = input("A random location: ")
print()
print("This story starts out with", name, "taking a walk in", location)
print()
print('Then all of a sudden a huge bout of', fear, "takes over", name)
print()
print('With a huge explosion of fog', enemy, "appears and says that", location, 'belongs to them and that', name, 'is on their turf')
print()
print('When hearing this', name, 'got angry and', fear, 'left and', name, 'used their power of', superPower, 'to defeat', enemy, 'and saved', location, 'from the wrath of', enemy)

'''

'''
print("Uh, oh, you've been given a", '\033[36m', 'warning', '\033[0m', 'for being a bad, bad person.')

'''








#Day 3 
'''
foodName = input("Name a food: ")
plantName = input("Name a type of plant: ")
cookingMethod = input("Name a method of cooking: ")
burnedFood = input("What word describes burned food?: ")
homeItem = input("Name a household item: ")

print("My favorite food is", cookingMethod, foodName, "with", burnedFood, plantName, "on a bed of", homeItem)

'''

'''

print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", name)
print("Who did something cool like", thing, "at the wonderful", place , "where you'll find me", rhyme)

'''







#Day 2

#my_Name = input("Name: ")

'''
myName = input("What is your name?: ")
myAge = input("How old are you?: ")
print("Gee, that's REALLY OLD")
replit = input("Do you like Replit?")
print("Of course you do!")
print() #extra print for spacing in console
print("So, you are")
print(myName)
print("and are the ripe old age of")
print(myAge)
print("and clearly think that Replit is")

'''
'''
myName = input("What is your name?: ")
myFood = input("What is your favorite food?: ")
myMusic = input("What is your favorite music?: ")
myLocation = input("Where do you live?: ")
print()
print("You are")
print(myName)
print("You're probably hungry for")
print(myFood)
print("and you're definitely getting your groove on to")
print(myMusic)
print("living in the amazing")
print(myLocation)

'''







#Day 1

print("Hello Replit")
print('How are you?')

print('''
Here's an exact
      BIT
       OF
        TEXT
''')

print('What could go wrong?') #print works & Print won't: case sensitive

print("Please work") #need to put quotes around the text

print('''
Frank
March 11th, 2024
I am signing up for Replit's 100 days of Python challenge!
I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day.
I'll be using Replit, an amazing online IDE so I can do 
this from my phone wherever I happen to be. No excuses 
for not coding from the middle of a field!
I am feeling 😃
You can follow my progress at replit.com/@F
''')

