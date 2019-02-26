'''
This is a way
to do multiple
line comments
'''

# take string translate language, in giraffe language all vowels are G

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
        # if letter in "aeiouAEIOU":
            # translation = translation + "g"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(raw_input("Enter a phrase: ")))
print
