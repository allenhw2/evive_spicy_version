# evive_spicy_version
# Evive_take_home

## Dependencies:
Found in requirements.txt

## Execution:
- To run the cycle once like the spec sheet use Evive_menu_single.py
- To cycle through multiple times until exit use Evive_menu_cycle.py
- to run tests use menu_tests.py


## Overview:
Since the assignment specifications called for object oriented programming, I went with a class structure for the menu and created separate classes for each meal type.
A simple alternative would be to have it all in one class that utilized nested dictionarys as the entire menu. One would then process the order and find the keys accordingly. 

One of the main things I tried to focus on while coding is the scalability of code. Especially since the concept is that of a menu, a menu adds and subtracts items all the time. However I had some diffculties in making it as easily scalable as it could without making food classes too complex. 

I originally had the code print directly from the classes, but in order to facilitate testing, I am having the classes return their outputs as strings which get printed in the main class. 

## Design:

### Evive_menu_cycle: 
- greets users and ask for input
- creates a Order object and populates the object
- prints out the string output statement from the Order object
- loops until user specifies to leave (or an exception is raised)
### Evive_menu_single:
- no greeting immediately ask for order
- prints order in the same fashion as above
- closes

### Classes:
- the main code for the individual classes
- Order Class:
    - Takes the string input and does checks to make sure it is valid
    - Creates and initializes the correct order type class
    - raises exceptions if formatting is invalid or the meal type is unknown
    - Print() returns the string output of the meal
- Breakfast/Lunch/Dinner Class:
  - takes order and populates the desired lists with the name of the item
  - gets the name from a dictionary menu that can be updated to add more items
  - Uses if statements to fit the requirements of each food type
  - if there are any invalid order, if adds the error type to the error list for later printing
  - When printing, checks to see if there were any errors in the list, if so it will return those out in the correct format as a string
  - if there were no errors, if will return a string in the desire format

- menu_tests:
  - runs through a pretty comprehensive set of inputs that might throw errors

