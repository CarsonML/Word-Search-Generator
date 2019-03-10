# Word-Search-Generator
A python script to generate word searches based off a config text file

# Word Search Inputs
The word search generator would take inputs from a config file stored as a text, in this form:

dimesion1 

dimension2

word1

word2

word3

...

# Creating the Word Search
First, I created an empty nested list with the size specified in the config file, filled with "/." These representented an empty space in the word search. I then created a function to choose a random position (that would allow the word to fit without going out of bounds) and try to put the word into the wordsearch in a random direction. It would try to write the word in that place and direction, and if it failed, it would choose another starting point and direction. It would fail if it was writing over an existing word. After creating this function, I started the process of making the word search. I first checked if the words would fit in the given dimensions, and gave an error if they did not. Otherwise, it would use the function to write in every word. Finally, It would fill in all empty spaces with random letters, and then print the word search in a readable format.

# Use of Copy Library
At one point in my code, I used the copy library instead of just setting two lists equal to eachother. I did this because in python, if lists are set equal, and one is modified, both lists end up being changed. I think this arises because lists are stored as a location in memory, and setting two equal sets their memory location to the same thing. Therefore, when one is changed, both lists reference the same changed object. This was causing my code to fail, since it relies on numerous attepmts to fit words, which require a copy of the working list to be modified. The use of the copy library to make a copy circumvents this issue.

Made while working with Hello World Studio
