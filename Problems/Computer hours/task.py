# Make sure your output matches the assignment *exactly*
hours = abs(int(input()))


def determiner(hours_spent):
    if hours_spent < 2:
        return "That seems reasonable"
    elif hours_spent < 4:
        return "Do you have time for anything else?"
    else:
        return "You need to get outside more!"


print(determiner(hours))
