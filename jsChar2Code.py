a = input("")
s = []
for l in a:
	s.append(str(ord(l)))

print("String.fromCharCode("+",".join(s)+")")
