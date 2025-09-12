# word game script 

# get a word from the user 
word = input("enter a word; ")

# find the length of the word
word_length = len(word)
print(f"the word '{word}' has {word_length} characters")

# reverse the word 
reverse_word = word[::-1]
print(f"the reverse word is: {reverse_word}")

# creating a new word by repeating the first character 
first_char = word[0]
new_word = first_char * word_length
print(f"the newly created word is: {new_word}")

# concatenate the original word with suffix
suffix = "ish"
word_with_suffix = word + suffix
print(f"the word with the suffix : '{suffix}':{word_with_suffix}")

# covert the word to uppercase 
my_new_word = word.upper()
print(f"this is the word in uppercase: {my_new_word}")

# replace a character in the word 
index = 0
replaced_word = word[:index] + "l" + word[index+1:] 
print(f"the replaced character is: {replaced_word}")