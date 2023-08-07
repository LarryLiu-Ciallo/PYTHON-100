a = 1
b = 1
raw = [a,b]
i=1
while i < 20:
    c = int(raw[i] + raw[i-1])
    raw.append(c)
    i = i + 1

print(raw)