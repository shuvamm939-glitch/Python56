#print welcome maessage(all types of print statements)
print("Hello World!")
print('Hello World!')

message = 'Hello World'

print(message)

message1 = "Shuvam's House"   #Option 1: Using double quotes to include double quote in string
print(message1)

message2 = 'Shuvam\'s House'   #Option 2: Using single quotes and escaping the apostrophe
print(message2)

message3 = """Shuvam's House"""  #Option 3: Using triple quotes to include single quote in string
print(message3)

message4 = '''Shuvam's House'''  #Option 4: Using triple quotes to include single quote in string
print(message4)



# len() function to get the length of a string
message5 = 'Hello World!'
print(len(message5))
print(message5[10])  # Accessing the last character of the string using indexing
print(message5[0:5])  # Accessing a substring from index 0 to 4
print(message5[6:12])  # Accessing a substring from index 6 to 11



# lower() and upper() methods to convert string to lowercase and uppercase
message6 = 'Hello World!'
print(message6.lower())
print(message6.upper())



#count() method to count the occurrences of a substring in a string
message7 = 'Hello World! Hello Everyone!'
print(message7.count('Hello'))  # Counting the occurrences of 'Hello' in the string
print(message7.count("l"))  # Counting the occurrences of 'l' in the string
print(message7.find('World'))  # Finding the index of the first occurrence of 'World' in the string



#replace() method to replace a substring with another substring in a string
message8 = 'Hello World! Hello Everyone!'
new_message = message8.replace('Hello', 'Hi').replace('World', 'Universe')  # Replacing 'Hello' with 'Hi' and 'World' with 'Universe' in the string
print(new_message)  # Printing the modified string
