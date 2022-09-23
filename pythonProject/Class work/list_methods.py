# import random
#
# lst = list(range(1,11))
# print(lst)
#random.shuffle(lst)
#
# print(lst)
# print(random.choice(lst))


#
# lst.append(20)
# print(lst)
#
# lst.append([20,30,40])
# print(lst)
#
# lst.extend([20,30,40])
# print(lst)
#
# lst += [20,30,40]
# print(lst)

# lst.insert(0,56)
# print(lst)
#
# last_item = lst.pop()
# print(last_item)
#
# item_at_index_0 = lst.pop(0)
# print(item_at_index_0)
# print(lst)
#
#
# lst.remove(8)
# print(lst)
#
# print(lst.count(5))
# print(lst)
#
# print("count",lst.count(4))
# print(lst)
#
#
#  lst.clear()
#  print(lst)
#
# print(lst.index(2))


# lst.reverse()
# print(lst)

# lst.sort()
# print(lst)

# lst.sort(reverse = True)
# print(lst)

def last_elem(string):
    return string[-1]

# fruits = ["banana", "apple", "cucumber", "mango", "grape"]
# fruits.sort(key=len)
# print(fruits)

# fruits = ["banana", "apple", "cucumber", "mango", "grape"]
# fruits.sort(key=last_elem)
# print(fruits)

# fruits = ["banana", "apple", "cucumber", "mango", "grape"]
# fruits.sort(key=last_elem, reverse=True)
# print(fruits)

def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

print(anagram("listen", "silent"))