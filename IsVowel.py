# text = input("Enter a character: ")
# if text.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(f"{text} is a vowel.")
# else:
#     print(f"{text} is not a vowel.")
# Take input from the user
text = input("Enter a word or sentence: ")


count = 0


for char in text.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print("Number of vowels:", count)