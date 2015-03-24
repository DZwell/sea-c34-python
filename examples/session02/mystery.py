def squirrel_party(cigars, weekend):
    """
    Return whether squirrel party is successful.

    Args:
        cigars (int): number of cigars smoked
        weekend (boolean): whether or not it is a weekend
    Return:
        whether there were between 40 and 60 cigars inclusive
        if on a weekday, and otherwise on weekends, you
        can't have enough cigars.
    """
    if (not weekend) and ((cigars >= 40) and (cigars <= 60)):
        return True
    else:
        return False

if __name__ == "main":
    if (squirrel_party(40, False)):
        print("Successful weekday party")
    else:
        print("It bombed.")

    if (squirrel_party(70, True)):
        print("Sky's the limit!")
    else:
        print("Sadface.")
