def find_prime():
    num = 0
    while num < 16:
        if not num % 2 == 0:
            yield num
            num += 1
        else:
            num += 1

    print('...StopIteration...')

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

a_pipeline = find_odd_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)