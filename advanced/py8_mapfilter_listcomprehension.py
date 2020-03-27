# 맵과 필터를 대신하는 리스트컴프리핸션
# map
st1 = [1, 2, 3]
st2 = list(map(lambda n: n ** 2, st1))
print(st2) #[1, 4, 9]
# list comprehension
st2 = [n ** 2 for n in st1]
print(st2) #[1, 4, 9]

# filter
st = [1, 2, 3, 4, 5]
ost = list(filter(lambda n: n % 2, st))
print(ost) #[1, 3, 5]
# list comprehension
ost = [n for n in st if n % 2]
print(ost) #[1, 3, 5]


# map & filter
st = list(range(1, 11))
fst = list(map(lambda n: n ** 2, filter(lambda n: n % 2, st)))
print(fst) #[1, 9, 25, 49, 81]
# list comprehension
fst = [n ** 2 for n in st if n % 2]
print(fst) #[1, 9, 25, 49, 81]