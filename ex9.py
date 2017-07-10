movie = ["movie 1", "movie 2", "movie 3"]
actor = ["actor 1", "actor 2", "actor 3"]
[(m+" is played by "+a) for (m, a) in zip(movie, actor)]

movies = dict(zip(movie, actor))

zipo = [(k+" is played by "+v) for (k, v) in movies.items()]

ko = 5

ex4 = [i*100 for i in range(1, 10) if (i % 2 == 0)]
[print(i) for i in ex4]
ex5 = [i*100 if (i % 2 == 0) else i for i in range(1, 10)]
print("ex5")
[print(i) for i in ex5]

sevenBoom = ['Boom!!' if (i % 7 == 0) else i for i in range(1, 100)]
print("Seven Boom")
[print(i) for i in sevenBoom]

sumFun = lambda a, b: a+b

print(sumFun(5, 3))

jouls= [5000, 8000, 10000, 6000, 12000]
tuppleee=tuple(zip(jouls, map(lambda j: j / 4184, jouls)))
print(tuppleee)

# all multiple (1,1) till (6,6)
multi = tuple([(a, b, a*b) for a in range(1, 7) for b in range(1, 7) if b >= a])
print(multi)
language = ["HTML","JavaScript", "Ruby", "Python"]
print(list(filter(lambda a: a == "Python", language)))

#return len(list(filter(lambda a: a in s, list(t)))) > 0


def is_anagram(s, t):
    return sorted(s)==sorted(t)


print(is_anagram('rat', 'car'))
print(is_anagram('rac', ''))
print(is_anagram('rat', 'cr'))





