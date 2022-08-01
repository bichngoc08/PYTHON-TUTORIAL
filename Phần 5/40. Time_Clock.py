
from time import time

print("Enter your name: ", end='')
start_time = time()
name = input()
elapsed = time() - start_time
print(name, ",it took you", elapsed, "seconds to respond")

start = time()
for i in range(10000):
    print(i, end='')
end = time()
duration = end - start
print("duration= ", duration)
