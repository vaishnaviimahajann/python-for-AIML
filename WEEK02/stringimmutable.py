word= "hello"
# word[0] = "H"  # This will raise an error because strings are immutable in Python.

word = "Python"
print(word[2:4])

word = word[:2] + "X" + word[3:]

print(word)

