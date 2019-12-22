word = "houses was here"

guessed_chars = ['o', 's', 'h', 'u', 'w']

word_split = list(word)

final_word = ""

#print(word_split)

for char in word_split:
	if char == " ":
		final_word += " "
		continue
	if char in guessed_chars:
		final_word += char
	else:
		final_word += "_"

print(final_word)