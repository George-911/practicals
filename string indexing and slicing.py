greeting = "hello, world!"
name = "Alice" 
# using the len() function to get the length of a string 
print(len(greeting)) 
print(len(name))

# indexing
print(greeting [0]) # outputs the first character in the string 
print(name[-1]) # outputs last character in the string
print(name[1])
 
# slicing
print(greeting[0:5]) # outputs hello
print(name [1:3]) # outputs li
print(greeting [::-1])  # outputs dlrow ,olleh
print(greeting [::-2])  # outputs !lo olh

# concertenation with '+'
full_name = name + "wonderland"
print(full_name)  # outputs Alicewonderland
full_name_space = name + ' ' + "wonderland"
print(full_name_space) #outputs Alice wonderland

# repetition with '*'
chant = name*3
print(chant) # outputs AliceAliceAlice

# using string methods 
print(greeting.upper())  # outputs HELLO, WORLD!
print(name .lower())   #outputs alice
print(name .replace('l','x'))