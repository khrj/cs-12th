print((s := input("Enter string: ")) and "".join([s[0], *[x if x != s[0] else '$' for x in s[1:]]]))
