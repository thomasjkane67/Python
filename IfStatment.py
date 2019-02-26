# Boolean variable
is_male = True
is_tall = False

if is_male or is_tall:
    print("You are a male, or tall ")
else:
    print("You are female, or short ")

def or_statement():
    is_male = False
    is_tall = False

    if is_male or is_tall:
        return "You are a male, or tall "
    else:
        return "You are female, or short "
result = or_statement()
print(result)

def and_statement():
    is_male = False
    is_tall = False

    if is_male and is_tall:
        return  "You are a male, and tall "
    else:
        return "You are female, and short "
result = and_statement()
print(result)

def elseif_statement():
    is_male = False
    is_tall = True

    if is_male and is_tall:
        return  "You are a male, and tall "
    elif is_male and not(is_tall):
        return "You are male and short"
    elif not(is_male) and is_tall:
        return "You are female and tall"
    elif not(is_male) and not(is_tall):
        return "You are female, and short "
result = elseif_statement()
print(result)