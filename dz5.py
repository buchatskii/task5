from datetime import datetime
import time

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start_time = datetime.now()
for i in src:
    if src.count(i) == 1:
        print(str(i) + ' ')

time.sleep(1) # Время измерить не удалось, поэтому замедлил код, для получения числа больше 0
skorost = datetime.now() - start_time
print(skorost)