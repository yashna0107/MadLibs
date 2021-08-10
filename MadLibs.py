"""Mad Libs generator
---------------------------
"""

#Loop back to this point once code ends

loop = 1
while loop < 10:
    #All the questions that the program asks the user
    noun = input("Choose a noun: ")
    plural_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Choose a place: ")
    adjective = input("Choose an adjective (describing word): ")
    noun3 = input("Choose a noun: ")

    #Displays the story based on users input
    print("----------------------------")
    print("Be kind to your ",noun,"- footed ", plural_noun)
    print("For a duck may be somebody's ", noun2, ",")
    print("Be kind to your ", plural_noun, "in ", place)
    print("Where the weather is always ", adjective)
    print()
    print("You may think this is the ", noun3," ,")
    print("Well it is! ")
    print("----------------------------")

    #Loop back to "loop=1"
    loop = loop + 1

