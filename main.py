import random

facts = [
    "1 in 5,000 north Atlantic lobsters are born bright blue.",
    "A skunk's smell can be detected by a human a mile away.",
    "You might be drinking water that is older than the solar system.",
    "Stop signs used to be yellow.",
    "Most wasabi we eat in the U.S. isn't really wasabi.",
    "The majority of your brain is fat.",
    "A crocodile cannot stick its tongue out."
  ]

print("Hello")
name = input("I am Chatbot. \nWhat is your name? \n")

print(f"Hello {name}\n")
wellBeing = input("How are you today?\n")

if wellBeing == "good" :
  print("Thats great to hear!")
  print("Personally I think today is a wonderful day.")

elif wellBeing == "bad" :
  print("Thats too bad, I hope that it gets better")

else :
  print("I see, thats an interesting way to feel.")
  
agreement = input("\nWould you like to hear a random fact?\n")

while agreement != "no" :
  
  if agreement == "yes":
    print("\nOk, did you know, ")
    print(random.choice(facts))
    agreement = input("\nWould you like to hear another fact? ")
    
  else :
    print("\nSorry I didn't get that")
    agreement = input("Would you like to hear a fact? ")

print("\nOk, have a great day!")