list = []
i = 1
for i in range(16):
    if i % 2 != 0:
        list.append(i)
        print(i)
    i += 1
print('...StopIteration...')