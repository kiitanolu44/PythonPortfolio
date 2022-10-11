# Ask the user to enter the names of everyone attending a party
# then return a lsit of the party guests in alphabetical order 

# break it down

# 1 ask the users to enter the names of everyone attending a party
# 2 put those values in a list
# 3 sort the list - using the sort function
# 4 print the sorted list



# Asking the user for everyone attending the party
partyAttendees = input("Name everyone who is attending the party (each name separated by a comma): ")

# Separate the list with a comma followed by a space to format the list and make it presentable to the user
partyAttendeesList = partyAttendees.split(', ')

# sort the list using the sort function (alphabetically)
partyAttendeesList.sort()

# Print the list so the user can clearly see all of the attendees in alphabetical order
print("Party Attendees : " , partyAttendeesList)