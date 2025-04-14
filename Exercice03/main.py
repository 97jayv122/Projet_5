words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = "aeiouy"
words = [(word, sum(word.count(vowel) for vowel in vowels)) for word in words]

print(words)