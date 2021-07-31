grade = int(input("Enter random grade: "))
location = input("Choose a location(ground, roof, lobby, corridor): ")
verb1 = input("Enter a verb in -ing form(activity): ")
verb2 = input("Choose a verb (kick, lick): ")
adjective1 = input("Enter a adjective(size): ")
noun1 = input("Enter a object: ")
noun2 = input("Enter another noun(that we wear): ")
verb3 = input("Enter a verb(feeling): ")
activity = input("Enter another verb in -ing form that represents activity: ")
curse = input("Enter a curse word: ")
body_part = input("Enter body part: ")
adjective2 = input("Enter another adjective: ")
fav_sub = input("Your Favourite Subject: ")
verb4 = input("Enter another verb in -ing form(activity): ")
verb5 = input("Enter another verb in -ing form: ")
food = input("Enter a food: ")
adjective3 = input("Enter another adjective that describe a person: ")

story = f"One time in {grade}th grade we were at {location} and while I was {verb1} to my friends, \
I just so happened to {verb2} a {adjective1} {noun1}. I was wearing {noun2} so it {verb3} \
like hell and without {activity}, I shouted at the top of my {body_part} '{curse}' And with \
my {adjective2} luck, my {fav_sub} teacher was {verb4} at the bench right beside me. He then took \
me inside to what I thought was yell at me but he just couldn’t stop {verb5} and sent me \
back outside with a literal {food}. He is still my {adjective3} teacher I’ve ever had."

print(story)
