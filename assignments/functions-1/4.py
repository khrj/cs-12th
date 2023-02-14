def unique(lst):
    seen = []
    unique = []

    for elm in lst:
        if elm not in seen:
            seen.append(elm)
            unique.append(elm)
        else:
            try:
                unique.remove(elm)
            except:
                pass

    return unique

    # return list(set(lst))
    # Make note: this is invalid. 
    # this will return a set, 
    # not a list of unique elements.
    #
    # For example, [1,2,3,4,5,5,5] has unique elements
    # [1,2,3,4] but forms set [1,2,3,4,5]


print(unique(input("Enter list separated by commas: ").split(",")))
