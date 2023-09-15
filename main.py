# Names: Gerardo Pinda, Jesus Ruiz, Sebastian Wong, Isaac Munguia

##################################### String Methods#################################
# # Splitting a string and join
# text = "Hello, World! World, world fugar mya"
# print(text[0])  # Prints H
# print(text[1])  # Prints e
# newString = text.split(",")
# print(newString)  # Prints ['Hello', 'World! World', ' world fugar mya']
# print(newString[0])  # Prints Hello
# print(newString[1])  # Prints World! World
# print(newString[-1])
# string3 = text.split(" ")
# print(string3)  # ['Hello,', 'World!', 'World', 'world', 'fugar', 'mya']
# print(string3[-1])  # prints mya
# string4 = text.split("d")
# print(string4)
# string5 = text.split("o")
# print(string5)

# finalString = " ".join(newString)
# print(finalString)

# String Methods Practice #1
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
# sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
sen1 = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sen1.upper())

# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
# word_list = ["Simple","is","better","than","complex."]
list = ["Simple", "is", "better", "than", "complex."]
final_list = " ".join(list)
print(final_list)

# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.
sen3 = "If the implementation is hard to explain, it might be a bad idea."
sen3a = sen3.replace("hard", "easy")
sen3b = sen3a.replace("bad", "good")
print(sen3b)

#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
print("Repitition " * 15)

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
haiku = "Whitecaps on the bay: A broken signboard banging In the April wind."
not_found = "beach" in haiku.lower()
# Print the boolean result
print(not_found)
# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
word = "electroencephalographist"
length = len(word)
print(length)
