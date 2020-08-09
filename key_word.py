# -*- coding；utf-8 -*-

'''
查找关键词的个数
出现频率不低于0.10
单词总数n  怎么判断单词是不是重复出现 有多少个单词，每个单词出现的次数
字典：查找的复杂度为O(1)
'''

# from collections import Counter
# n = int(input())
# sentence = ''
# for i in range(n-1):
#     sentence += input() + ' '
# sentence += input()
# #print(sentence)

# counts = Counter(sentence.split())
# #print(counts)

n = int(input())
sen_dict = {}
#创建单词及其出现个数的字典
for i in range(n):
    word = input().lower()
    if word not in sen_dict:
        sen_dict[word] = 1
    else:
        sen_dict[word] += 1

key_word_nmber = 0
for i in sen_dict.keys():
    if (sen_dict[i]/n) >= 0.01:
        key_word_nmber += 1
print(key_word_nmber)