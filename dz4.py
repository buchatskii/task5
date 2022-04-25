src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
i = 1
while i < len(src):
    if src[i] > src[i-1]:
        print(src[i])
    i += 1