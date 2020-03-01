#Comma Code
#
#
#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
#with and inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
#But your function should be able to work with any list value passed to it.
#Be sure to test the case where an empty list [] is passed to your function.

list = ['apples', 'bananas', 'tofu', 'cats']

def awesome(spam):
    for n,i in enumerate(spam):# Where "n" it's the index number of the item and "i" the name
        print(i + ", ", end="")
        if n == (len(spam)-2): # If it's the before last item, print an "and"
            print("and ", end="")
            break
    print(spam[len(spam)-1])   # Writes the last missing item from the list
    
awesome(list)





