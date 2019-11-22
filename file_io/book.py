# Importing the regular expression library and the collections library
import re
import collections

#Open the file, reads it to the variable text, set it all to lower case
text = open('file_io/book.txt', encoding="utf8").read().lower()

# use the regular expression function final all
# \w+ = the w denotes anything that's not a white space, and the plus denotes one or more
words = re.findall('\w+', text)

# Prints out, using the collections method 'counter', from the variable words, the most common 10 words
print(collections.Counter(words).most_common(10))