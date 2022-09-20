# s = "Python is very very simple "
# d = {}
# for word in s.split():
#     if word in d.keys():
#         d[word] += 1
#     else:
#         d[word] =1
# print(d)
#
# s = "Python is very very simple "
# d = {}
# for word in s:
#     if word in d.keys():
#         d[word] += 1
#     else:
#         d[word] =1
# print(d)
#
# s = "Python is very very simple "
# d = {}
# for word in s.split():
#     if word not in d.keys():
#         d[word] = len(word)
# print(d)


# l =['Boston Americans', 'New York Giants', 'Chicago White Sox', 'Chicago Cubs', 'Chicago Cubs', 'Pittsburgh Pirates', 'Philadelphia Athletics', 'Philadelphia Athletics', 'Boston Red Sox', 'Philadelphia Athletics', 'Boston Braves', 'Boston Red Sox', 'Boston Red Sox', 'Chicago White Sox', 'Boston Red Sox', 'Cincinnati Reds', 'Cleveland Indians', 'New York Giants', 'New York Giants', 'New York Yankees', 'Washington Senators', 'Pittsburgh Pirates', 'St. Louis Cardinals', 'New York Yankees', 'New York Yankees', 'Philadelphia Athletics', 'Philadelphia Athletics', 'St. Louis Cardinals', 'New York Yankees', 'New York Giants', 'St. Louis Cardinals', 'Detroit Tigers', 'New York Yankees', 'New York Yankees', 'New York Yankees', 'New York Yankees', 'Cincinnati Reds', 'New York Yankees', 'St. Louis Cardinals', 'New York Yankees', 'St. Louis Cardinals', 'Detroit Tigers', 'St. Louis Cardinals', 'New York Yankees', 'Cleveland Indians', 'New York Yankees', 'New York Yankees']

from collections import Counter
# c = Counter(l)
# print(c)

from collections import Counter
l = [1,2,3,4,1,12,1,3,4,5,1,2,3,4,1,2,3,4,]
c =  Counter(l)
print(c)