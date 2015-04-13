# this is the file for donorletters code

# add note when safe_input.py completed

d = {"mary": [50], "josh": [50], "cassie": [34]}

print d
d["mary"] = 100
print d

# ok, this method overwrites the existing donation amt. how can I add an amt?

d["mary"] = [d["mary"], 50]
print d
print d.keys()
print d["mary"]
print type(d["mary"])
print d["mary"][0]
print type(d["mary"][0])
print d["mary"][1]

# now I can add an amt & create a tuple that I can then call via place number.
# let's make this a function


def addamt(name, dict, amt):
    for key, value in dict.items():
        if key == name:
            dict[key] = dict[key] + [amt]
        elif name not in dict.keys():
            dict[name] = [amt]
    return dict

addamt("mary", d, 45)
addamt("OC", d, 1000)
addamt("josh", d, 56)
print d

print d["mary"][0]
print d["mary"][1]

# SO BEAUTIFUL DO NOT TOUCH.


"""
def sendletter(name, dict):
    if name in dict:
        # proceed
    elif name not in d:
        # add it

def mainmenu():
    action = raw_input("Would you like to 'SEND' a thank you note," +
                       " 'CREATE' a report, or 'QUIT'?")
    while action.upper() != "QUIT":
        if action.upper() == "SEND":
            action = raw_input("Please enter a full name, 'LIST' for options,"+
                               " or 'MENU' to go back")
            while action.upper() != "MENU":
                sendletter(action)
            else:
                mainmenu()
    else:
        exit()

"""


"""
if action == SEND:



        if name == "MENU"":

            go back to action prompt

        if name == "LIST"":

            print donorlist.keys #names

            name = raw_input("Please enter a name from the list,
                or type a new one to add"")

        while name not in donorlist.keys:

            ask if they want to add the name y/n

                if y, add name to donorlist

                if no, ask for name again

        if name in donor list.keys:

            name.value = int(raw_input(ask for donation amount))

            while name.value is not an int,

                ask for name.value again

            add (name,value) to donorlist
            #how to add multiple donations to one user?

    def createletter(name,value):

        print "Dear %n, thank you for your generous donation of %v.
        We appreciate your support of our mission, which enables us to provide
        essential services to hundreds of Seattle families.
        Sincerely, do great inc."" %n name %v value

    createletter(name,value)

    name = MENU

if action == create:

    def createreport():

        sort donorlist by donation amount

        print donorlist.keys, sum(donorlist.values), count(donorlist.values)
         and average(donorlist.values)

    # return to main menu

    # action = raw_input("Would you like to SEND a thank you note,
        CREATE a report, or QUIT?")
"""
