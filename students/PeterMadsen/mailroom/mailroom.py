def main():
    """
    This is the main program loop that runs until the user quits

    Asks user's what they would like to do. Directs the flow of the flow of
    the program to the correct locations. 
     
    """

    # Set up
    donors_dictionary = {}
    #add features to donors_dictionary
    prompt = "Some appropriate string"

    while user is not Done:
        input = get_user_input(prompt)

        if input == thank_you:
            thank_you(donors_dictionary)
        elif input == create_report:
            create_report(donors_dictionary)
        elif input == 'list':
            for key in donors_dictionary: print key
        elif input == 'quit':
            print ("Have a good day!")
            break
        else:
            print ("That is not a valid answer")

def thank_you(donors_dictionary):
    """
    Updates Donor data structure and prints thank you message.

    Args:
        donors_dictionary (dictionary) : contains donors as keys and donations
        amounts as a list
    Return: 
        None 

    Allows user to add new donors to the donor data structure. Also allows
    user to enter new donations. Once the user has been able to do that, a 
    message is automatically generated as a response or the donation.Set

    """
    prompt = "Please enter the donor’s full name: "
    input = get_user_input(prompt)
    
    while input == 'list':
        print(donors_keys)
        input = get_user_input(prompt)
    
    if input not in donors_keys:
        donors_dictionary[input] = []
      
    dontation_amount = get_user_input("Donation Amount", True)
    donors_dictionary[input] += [dontation_amount]
    
    print "some sweet email"


def create_report(donors_dictionary): 
    """
    Prints message containing a report of donations for each donor. 
    
    Args:
        donors_dictionary (dictionary) : contains donors as keys and donations 
        amounts as a list
    Return: 
        None 

    Report calculates the total donation amount, the total number of donations,
    and the average donation amount for each donor and then displays  them 
    in a column like format. After the report has been printed the user is 
    returned to the original query. 

    """
    donor_totals_list = []
    
    for donor in donors_dictionary:
        total_donation = 0
        for num in donors_dictionary[donor]: 
            total_donation += num
            donor_totals_list  += [[total_donation, donor]]
    
    sorted_donor_list = sorted(donor_totals_list)
    sorted_donor_list.reverse() 
    
    for donor in sorted_donor_list:
        donation_number = len(donors_dictionary[donor[1]])
        average_donation = total_donation / donation_number
        print (formatted_donor_string)
    
def get_user_input(prompt, validator=None):
        """
        Request input from the user with `prompt` and return the result

        optionally, validate the input with a function `validator` which must
        take one argument, the input from the user and must return the input if
        valid, and None if not valid
        """
        reply = None
        while reply is None:
            reply = ask_for_input(prompt)
            if there_is_a_validator:
                validate_the_reply
        return reply

if __name__ == '__main__':
    main()