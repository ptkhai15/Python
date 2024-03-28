range(0,15)
print(*range(0,15))\\1 2 3 .. 14
print(*range(15)) \\1 2 3 4 5 6 .. 14
print(*range(3,30,4)) \\3 7 11 15 19 23 27
range(3,10,5,5)	\\error
print(*range(30,0)) \\error
print(*range(30,0,-1)) \\30 29 28 .. 1

