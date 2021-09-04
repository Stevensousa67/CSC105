words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
new_word = []
past_tense = []

for word in words:
    if word[-1] != 'e':
        new_word.append(word + "ed")
    else:
        past_tense.append(word + "d")

print(new_word)
print(past_tense)
