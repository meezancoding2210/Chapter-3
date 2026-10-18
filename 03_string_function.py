name = "Meezan"
print(len(name))  # Print the length of the string

print(name.endswith("an")) # Check if the string ends with "an"
print(name.startswith("Me")) # Check if the string starts with "Me"

a = "jojo's bizzare adventure"
print(a.capitalize()) # Capitalize the first letter of the string

print(a.upper()) # Convert the string to uppercase

b = "JOJO'S BIZZARE ADVENTURE"
print(b.lower()) # Convert the string to lowercase

count = a.count("jo")
print(count) 

print(a.title()) # Convert the first letter of each word to uppercase

index = a.find("adventure") # Find the index of the substring "adventure"
print(index)

replace = a.replace("jojo", "jotaro")
print(replace.capitalize()) # Replace "jojo" with "jotaro" then capitalize the first letter of the new string

c = "   jojo's bizzare adventure   " 
print(c.strip()) # Remove leading and trailing whitespace from the string

d = "34"
print(d.zfill(5)) # Pad the string with zeros on the left to make it 5 characters long

print(a.isalpha()) # Check if the string contains only alphabetic characters
print(d.isdigit()) # Check if the string contains only digits

e = "user0123"
print(e.isalnum()) # Check if the string contains only alphanumeric characters