import random
from nums_kor import *

hour_index = random.randint(0,len(hours_kor)-1)
hour_real = hour_index + 1

print(f"Korean time: {hours_kor[hour_index]} 시")
print(f"Numeric time: {hour_real}:00")
# time = input("What time is this? ")