# def print_rangoli(size):
#     # your code goes here
#     col = 4 * size - 3
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     lst = []
#     for i in range(size - 1, -1, -1):
#         text = "-".join(alphabet[i:size][::-1])
#         text = f"{text}{text[::-1][1:]}"
#         # print(text)
#         lst.append(text.center(col, "-"))
#     lst.extend(lst[:-1][::-1])
#     for l in lst:
#         print(l)
#     return "\n".join(lst)
# "".title
# print("12abc  hell".title())
# print_rangoli(5)


# from collections import Counter


# def minion_game(string):
#     s = string
#     Stuart = Kevin = 0
#     # substrings = Counter(
#     #     [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
#     # )
#     for i in range(len(s)):
#         for j in range(i+1,len(s)+1):
#             if s[i:j][0] in "AEIOU":
#                 Kevin += 1
#             else:
#                 Stuart += 1
    
#     print(f"Stuart = {Stuart}" if Stuart>Kevin else f"Kevin = {Kevin}" )

#     print(Kevin)
#     print(Stuart)


# # Output: ['c', 'co', 'con', 'cond', 'o', 'on', 'ond', 'n', 'nd', 'd']
# minion_game("BANANA")


def merge_the_tools(string, k):
    # your code goes here
    s=len(string)//k
    data=[]
    for i in range(0,len(string),s):
        word=string[i:i+s]
        newword=""
        for w in word:
            if w not in newword:
                newword+=w
        data.append(newword)
    for d in data:
        print(d)
merge_the_tools("AABCAAADA",3)