import random

def template1():
    Number = input("Input a number: ")
    MeasureOfTime = input("Input a measure of time: ")
    ModeOfTransportation = input("Input a mode of transportation: ")
    Adjective = input("Input an adjective: ")
    Adjective2 = input("Input an adjective: ")
    Noun = input("Input a noun: ")
    Color = input("Input a color: ")
    PartOfTheBody = input("Input a part of the body: ")
    Verb = input("Input a verb: ")
    Number2 = input("Input a number: ")
    Noun2 = input("Input a noun: ")
    Noun3 = input("Input a noun: ")
    PartOfTheBody2 = input("Input a part of the body: ")
    Noun4 = input("Input a noun: ")
    Adjective3 = input("Input an adjective: ")
    SillyWord = input("Input a silly word: ")
    print(
        f"It was about {Number} {MeasureOfTime} ago when I arrived at the hospital in a {ModeOfTransportation}." 
        f"The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here."
        f"There are nurses here who have {Color} {PartOfTheBody}."
        f" If someone wants to come into my room I told them that they have to {Verb} first."
        f" I've decorated my room with {Number2} {Noun2}."
        f" Today I talked to a doctor and they were wearing a {Noun3} on their {PartOfTheBody2}."
        f" I heard that all doctors {Verb} {Noun4} every day for breakfast."
        f" The most {Adjective3} thing about being in the hospital is the {SillyWord} {Noun} !"
    )

def template2():
    ProperNoun = input("Input a proper noun(person's name): ")
    Noun = input("Input a noun: ")
    Adjective = input("Input an adjective(feeling): ")
    Verb = input("Input a verb: ")
    Adjective2 = input("Input an adjective(feeling): ")
    Animal = input("Input an animal: ")
    Verb2 = input("Input a verb: ")
    Color = input("Input a color: ")
    Verb3 = input("Input a verb + ing: ")
    Adverb = input("Input an adverb ending in ly: ")
    Number = input("Input a number: ")
    MeasureOfTime = input("Input a Measure of Time: ")
    SillyWord = input("")
    Noun2 = input("")
    print(
        f"This weekend I am going camping with {ProperNoun}. I packed my lantern, sleeping bag, and {Noun}."
        f" I am so {Adjective} to {Verb} in a tent."
        f" I am {Adjective2} we might see a(n) {Animal}, I hear they're kind of dangerous."
        f" While we're camping, we are going to hike, fish, and {Verb2}."
        f" I have heard that the {Color} lake is great for {Verb3}."
        f" Then we will {Adverb} hike through the forest for {Number} {MeasureOfTime}."
        f" If I see a {Color} {Animal} while hiking, I am going to bring it home as a pet!"
        f" At night we will tell {Number} {SillyWord} stories and roast {Noun2} around the campfire!!"
    )

def template3():
    ProperNoun = input("Input a proper noun(person's name): ")
    Adjective = input("Input an adjective(feeling): ")
    Color = input("Input a color: ")
    Animal = input("Input an animal: ")
    Place = input("Input a place: ")
    Adjective2 = input("Input an adjective(feeling): ")
    MagicalCreature = input("Input magical creatur (plural): ")
    Adjective3 = input("Input an adjective(feeling): ")
    MagicalCreature2 = input("Input magical creatur (plural): ")
    RoominaHouse = input("Input a room in a house: ")
    Noun = input("Input a noun: ")
    Noun2 = input("Input a noun: ")
    Noun3 = input("Input a noun(plural): ")
    Adjective4 = input("Input an adjective: ")
    Noun4 = input("Input a noun: ")
    Number = input("Input a number: ")
    Measureoftime = input("Input a Measure of Time: ")
    Verb = input("Input a verb ending with ing: ")
    Adjective5= input("Input an adjective: ")
    Noun5 = input("Input a noun: ") 
    print(
        f"Dear {ProperNoun}, I am writing to you from a {Adjective} castle in an enchanted forest."
        f" I found myself here one day after going for a ride on a {Color} {Animal} in {Place}."
        f" There are {Adjective2} {MagicalCreature} and {Adjective3} {MagicalCreature2} here!"
        f" In the {RoominaHouse} there is a pool full of {Noun}."
        f" I fall asleep each night on a {Noun2} of {Noun3} and dream of {Adjective4} {Noun4}."
        f" It feels as though I have lived here for {Number} {Measureoftime}."
        f" I hope one day you can visit, although the only way to get here now is {Verb} on a {Adjective5} {Noun5}!!"
    )

template = input("Choose a template from 1 to 3: ")
if template == "1":
    template1()
elif template == "2":
    template2()
elif template == "3":
    template3()
else:
    print("Ivalid option. Randomly choosing one for you...")
    random.choice([template1, template2, template3])()
    
    