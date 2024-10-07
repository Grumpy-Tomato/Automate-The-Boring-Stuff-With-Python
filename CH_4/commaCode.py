def stringFromList(list = []):
    if list == []:
        return "Nope, no list here, sorry pal"
    else:
        newString = ""
        for i in list:
            if i == list[-1]:
                newString += 'and %s.' % i
            else:
                newString += '%s, ' % i
        return newString



print(stringFromList(["You're", 'a', 'nerd', 'get rekt']))
print(stringFromList([]))