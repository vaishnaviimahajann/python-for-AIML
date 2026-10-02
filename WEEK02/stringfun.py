
# MODULE 3: PYTHON STRINGS

text = "hello python"
print("Original string:", text)

# 1. BASIC FUNCTIONS
print(len(text))             # Length of string
print(type(text))            # Data type
print(str(123))              # Convert to string

# 2. INDEXING
word = "Python"
print(word[0])               # P
print(word[-1])              # n

# 3. SLICING
print(word[1:4])             # yth
print(word[:3])              # Pyt
print(word[2:])              # thon
print(word[::2])             # Pto
print(word[::-1])            # nohtyP

# 4. CASE CONVERSION
print(text.upper())          # HELLO PYTHON
print(text.lower())          # hello python
print(text.capitalize())     # Hello python
print(text.title())          # Hello Python
print("PyThOn".swapcase())   # pYtHoN
print("HELLO".casefold())    # hello

# 5. SEARCHING AND COUNTING
print("banana".find("na"))   # 2
print("banana".rfind("na"))  # 4
print("banana".index("a"))   # 1
print("banana".count("a"))   # 3
print("python".startswith("py"))  # True
print("python".endswith("on"))    # True

# 6. REMOVING WHITESPACE
print("  hi  ".strip())      # hi
print("  hi  ".lstrip())     # hi
print("  hi  ".rstrip())     # hi

# 7. REMOVING PREFIX AND SUFFIX
print("unhappy".removeprefix("un"))  # happy
print("notes.txt".removesuffix(".txt"))  # notes

# 8. REPLACING
print("banana".replace("a", "o"))  # bonono

# 9. SPLITTING STRINGS
print("red blue green".split())     # ['red', 'blue', 'green']
print("a-b-c".rsplit("-", 1))       # ['a-b', 'c']
print("a\nb".splitlines())          # ['a', 'b']

# 10. PARTITIONING
print("a-b-c".partition("-"))       # ('a', '-', 'b-c')
print("a-b-c".rpartition("-"))      # ('a-b', '-', 'c')

# 11. JOINING
print("-".join(["a", "b", "c"]))    # a-b-c

# 12. ALIGNMENT AND FORMATTING
print("hi".center(6, "-"))          # --hi--
print("hi".ljust(5, "-"))           # hi---
print("hi".rjust(5, "-"))           # ---hi
print("42".zfill(5))                # 00042
print("Hello, {}".format("Sam"))    # Hello, Sam

name = "Sam"
age = 20
print(f"My name is {name} and I am {age}.")

# 13. CHECKING STRING CONTENT
print("Python".isalpha())      # True
print("123".isdigit())         # True
print("123".isdecimal())       # True
print("123".isnumeric())       # True
print("Python123".isalnum())   # True
print("hello".islower())       # True
print("HELLO".isupper())       # True
print("Hello World".istitle()) # True
print("   ".isspace())         # True
print("my_var".isidentifier()) # True
print("Hello".isprintable())   # True
print("Python".isascii())      # True

# 14. STRING OPERATORS
print("Py" + "thon")           # Python
print("ha" * 3)                # hahaha
print("Py" in "Python")        # True
print("Java" not in "Python")  # True
print("hi" == "hi")            # True
print("hi" != "Hi")            # True

# 15. STRING IMMUTABILITY
word = "Python"
word = "J" + word[1:]
print(word)                    # Jython

# 16. LOOPING THROUGH A STRING
for ch in "cat":
    print(ch)                  # c, a, t on separate lines