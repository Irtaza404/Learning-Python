
# import re

# text = "I have 3 cats and 12 dogs and 100 birds"
# result = re.findall("\\d+", text)
# print(result)
# # special character

# # .  → any character
# # \d → digit
# # \D → not digit
# # \w → word character
# # \W → not word character
# # \s → whitespace
# # \S → not whitespace# 

# # quantifier
# # *     → 0 or more
# # +     → 1 or more
# # ?     → optional
# # {n}   → exactly n
# # {n,m} → between n and m

# # anchors
# # ^   → start of string
# # $   → end of string
# # \b  → word boundary
# # \B  → NOT word boundary

# import re

# text = "hello world hello"
# result = re.findall("^hello", text)
# print(result)


# # character classes

# # [a-z]   # any lowercase letter
# # [A-Z]   # any uppercase letter
# # [0-9]   # any digit — same as \d
# # [a-zA-Z]        # any letter
# # [a-zA-Z0-9]     # any letter or digit — same as \w

# # # ^ inside [] means NOT these characters
# # [^aeiou]    # any character that is NOT a vowel
# # [^0-9]      # any character that is NOT a digit
# import re

# text = "Hello World 123"
# result = re.findall("[A-Z][a-z]+", text)
# print(result)

# CHARACTERS:
# .       any character
# \d      digit
# \D      not digit
# \w      word character
# \W      not word character
# \s      whitespace
# \S      not whitespace

# QUANTIFIERS:
# *       0 or more
# +       1 or more
# ?       0 or 1
# {n}     exactly n
# {n,m}   between n and m
# {n,}    n or more

# ANCHORS:
# ^       start of string
# $       end of string
# \b      word boundary
# \B      not word boundary

# GROUPS:
# ()      group
# (?P<name>) named group
# |       or

# CHARACTER CLASSES:
# [abc]   any of a,b,c
# [a-z]   range
# [^abc]  not a,b,c

# FLAGS:
# re.I    case insensitive
# re.M    multiline
# re.S    dot matches newline
# re.X    verbose

# FUNCTIONS:
# match()     start only
# search()    first anywhere
# findall()   all matches
# finditer()  all with positions
# sub()       replace
# split()     split by pattern
# compile()   reusable pattern

import re
def extract_dates(date):
    date=re.search("(\d+)/(\d+)/(\d+)",date)
    print(date.group())
extract_dates("Today is 04/07/2026")


bad_words = ["bad", "awful", "terrible"]
text = "This is a bad and terrible movie"
text=re.sub(r"\b"+"|".join(bad_words)+r"\b",lambda m :"*"*len(m.group(0)),text)
print(text)























