"""
\t: is Tab
\n: is newline
use underscores in large digits to make them more readable, but python won't print them.  e.g., 1_000_000 would print as 1000000
you can assign multiple variables to multiple values in one line., e.g., a, b, c = 1, 2, 3

all caps var names indicates they should be treated as constants (Python doesn't have built in constants)



Methods:
.rstrip() strips whitespace on right
.lstrip() strips whitespace on left
.strip() strips whitespace on left and right
.removeprefix() - whatever is added into () is removed (like 'https://' on a url)

Lists: 
variable = [listItem1, listItem2]
index an item by writing print(listName[0])
add a method to an item in a list e.g., print(listName[0].title())  (to titalize the item)
to append a list - listName.append('newItem') - adds a new item to the end of the list
to append an item elsewhere in the list - listName.insert(0, 'newItem') - inserts item at index 0
to remove an item from a list use del listName[0] - deletes first item in the list
you can also use the pop() method to remove the last item in a list and continue using it
e.g., poppedList = variable.pop()
print(poppedList) will print listItem2
to get rid of a certain item, use remove.  e.g., listName.remove('itemName')
    if there are multiple occurances, remove will only get rid of the first occurance

"""





first_name = "Lindsey"
last_name = "Wachtel"
full_name = f"{first_name} {last_name}"
print(full_name)

print('I would like to say, "Hello, world"')