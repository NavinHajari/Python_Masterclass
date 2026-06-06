#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

# backwards = letters[25::-1] # Backward slicing
backwards = letters[::-1]   # Same output as above (Python idioom for reversing a string)
print(backwards)

# Create a slice that produces the characters qpo
print(letters[16:13:-1])

# Create a slice that produces edcba
print(letters[4::-1])

# Create a slice that produces last 8 characters in reverse order
print(letters[:-9:-1])

# Create a slice to produce last 4 characters
print(letters[-4:])

# Create a slice to produce the last character
print(letters[-1:])

# Create a slice to produce the first character
print(letters[:1]) # Returns a empty string when the string is empty
print(letters[0])  # Returns "Index out of range" error for an empty string