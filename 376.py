s = input()
c = input()

first = s.find(c)
last = s.rfind(c)

result = s[:first] + s[last:first - 1:-1] + s[last + 1:]
print(result)