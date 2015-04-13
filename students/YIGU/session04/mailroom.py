# This python script helps mailroom to print Thank you letter to donor and
# create reports.

# Assuming donor names are unique because task7 asked "If the user types
# a name not in the list, add that name to the data structure and use it."
from collections import OrderedDict

# donner data
donor_his = {}
cr = {}


def safe_input(note):
    """This function catch excepitions from raw_input function and return\
     None"""
    try:
        i = raw_input(note)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return i


def is_number(n):
    try:
        float(n)
    except (ValueError):
        return False
    else:
        return float(n)


def send_thank_you_letters():
    """This function let you input donation amonut to donor history and \
    format a thank you letter with donor's name and donation amount."""
    while True:
        styl_prompt = safe_input(
            u"\nEnter donor's Full Name for donation;\n"
            "Enter LIST to list out all donors;\n"
            "enter RETURN to return to the original prompt-->")
        if styl_prompt == u'RETURN':
            break
        elif styl_prompt == u'LIST':
            print donor_his.keys()
        elif styl_prompt not in donor_his:
            print u'Adding %s to donor list\n' % styl_prompt
            donor_his[styl_prompt] = []
            add_donation(styl_prompt)
        else:
            add_donation(styl_prompt)


def print_thank_you_letter(styl_prompt):
    """This function print thank you letters"""
    "Dear {name},\n Thank you for your generous donation of {amonut}.\n"
    "MR".format(**{'name': styl_prompt, 'amonut': donor_his[styl_prompt][-1]})


def add_donation(styl_prompt):
    """This function is use by send_thank_you_letters to add donation to \
    donor_his. Function ask for donors_amount; make sure input is \
    int/float"""
    while True:
        add_d_prompt = safe_input(
            u"\nPlease enter donation amount;\n"
            "Enter RETURN to return to upper level-->")
        if add_d_prompt == u'RETURN':
            break
        elif is_number(add_d_prompt) is False:
            print "I don't know what is %s.\n" % add_d_prompt
            print "Please enter a number.\n"
        elif is_number(add_d_prompt) <= 0:
            print "Donation should be greater than 0. Please try again.\n"
        else:
            # store donation data in donor history
            add_d_prompt = float(add_d_prompt)
            donor_his[styl_prompt].append(add_d_prompt)
            print_thank_you_letter(styl_prompt)
            break


def create_report():
    """This function create report out of donor hisotry and sort by\
     total of donation amount"""
    cr = OrderedDict(sorted(donor_his.items(), key=lambda x: sum(x[1]), reverse=True))
    for i in cr:
        print "\nDonor name: %s," % i
        print "Total donation: %s," % reduce(lambda x, y: x + y, cr[i])
        print "Number of donation: %s," % len(cr[i])
        print "Average donation %s\n" % (reduce(lambda x, y: x + y, cr[i])/len(cr[i]))

if __name__ == '__main__':
    """This function work as the main startup menu"""
    while True:
        main_prompt = safe_input(
            u"\nWelcome! Enter 1 to send thank you emails\n"
            "Enter 2 to create a report; \n"
            "Enter EXIT to exit the progarm-->")
        if main_prompt == u'EXIT':
            break
        elif main_prompt == '1':
            send_thank_you_letters()
        elif main_prompt == '2':
            create_report()
        else:
            print "I don't know what is %s. Please try again.\n" % main_prompt
