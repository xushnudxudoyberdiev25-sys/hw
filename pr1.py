def count_vowels_and_consonants(text: str) -> dict:
    text = text.lower()
    unli = 0
    undosh = 0
    for word in text:
        if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
            unli += 1
        elif word.isalpha():
            undosh += 1
    return {"unli": unli, "undosh": undosh}

print(count_vowels_and_consonants("Salom Dunyo!"))