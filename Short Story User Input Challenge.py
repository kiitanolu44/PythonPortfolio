#collet variables from user to customise short story
#and display various answers

#[variable = input("question? ")]
#[variable = variable.capitalize()]
# > for capitalization of first character of user input variable
from atexit import register


Name = input("What is your Name? ")
Name = Name.capitalize()
HomeTown = input("What is the name of the town or city you currently live in? ")
HomeTown = HomeTown.capitalize()
FavouriteBakeryItem = input("What is your favourite bakery item? ")
BossName = input("What is the first name of your boss? ")
BossName = BossName.capitalize()
BossSheHeThey = input("what is your boss' pronouns? options are as follows [She/He/They]. ")
HalfMarathonTime = input("What is the best time you think you could complete a half marathon in? [in minutes] ")
CoName = input("What is the first name of your closest friend? ")
CoName = CoName.capitalize()
CoSheHeThey = input("What are their assigned pronouns? options are as follows [She/He/They]. ")
CoNameArea = input("What country are they from? [must be different from your own country or the country you currently reside]. ")
CoNameArea = CoNameArea.capitalize()

text = f"""
Dear Diary, 

Today was a good day, taking into account that I have not thrown up or seen {CoName}
since last week, ESPECIALLY after what happened and the way she behaved that night. 
I know {CoName} is from {CoNameArea}, but that is not an excuse to behave the way 
{CoSheHeThey} did. It’s worse, because everyone is looking at me funny, due to the 
fact that, I do not want to associate myself with {CoName} any more. It hurts, because, 
prior to this  {CoName} and I got on extremely well. We had even made plans, to begin 
training for the yearly half marathon together. Oh well.

I have been feeling poorly since I had some of {CoName}’s mother’s {CoNameArea}ean 
food or however you pronounce it. I’m not going to attribute it to that & that alone, 
but, it is a weird coincidence. She’s so lovely though, I’m going to miss her a lot.

Work has been going really well. They don’t call us {HomeTown}’s best bakery for nothing.
I just recently learnt how to make a {FavouriteBakeryItem} and I am chuffed! {BossName} 
(my boss) said my progress is astounding and {BossSheHeThey} is thinking about promoting 
me to assistant manager in a couple of months. All in all, things are good. I will keep 
you guys updated on how the marathon goes, hope fully this year I can beat my personal 
best of {HalfMarathonTime} minutes ahahaha.

Many Thanks

{Name}
"""
print(text)