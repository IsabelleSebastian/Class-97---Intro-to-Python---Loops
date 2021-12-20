intro = str(input("Please Introduce Yourself Here"))

wordcount = 1
charactercount = 0
nospacecount = 0

for i in intro:
    charactercount += 1

    if(i != " "):
        nospacecount += 1

    if(i == " "):
        wordcount += 1
print("Word Count:" , wordcount)
print("Character Count:" , charactercount)
print("Characters Excluding Spaces" , nospacecount)


