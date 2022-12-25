def count_words(text):
 words = text.split()
 counts = {}
 for word in words:
   if word in counts:
     counts[word] += 1
   else:
     counts[word] = 1
 return counts

print(count_words("text"))