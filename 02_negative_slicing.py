name = "Meezan" 

print(name[-5:-1]) #-1 not included
print(name[1:5])  #5 not included

print(name[:4]) #0 to 3, same as name[0:4]
print(name[2:]) #2 to end of string, same as name[2:6]

#Slicing with skip value 
word = "amazing"
print(word[1:6:2])  # Start at index 1, go up to index 5, and take every 2nd character

