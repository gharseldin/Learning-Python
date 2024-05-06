word = ["apple", "banana", "pear", "date", "tangerine"]

sorted_words = sorted(word, key=lambda w: w[len(w)-1], reverse=False)

print(sorted_words)
