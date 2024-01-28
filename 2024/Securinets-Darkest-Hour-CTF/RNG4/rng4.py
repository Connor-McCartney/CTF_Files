# rng 4
from random import Random,shuffle
import os

flag=os.environ.get('FLAG', 'FLAG{REDIRECT}').encode()
r1=Random()
Random_List=[r1.getrandbits(32) for i in range(625)]
choice=int(input("Choose an index to leak from 0 to 623"))
assert choice>=0 and choice <624
print(f"Leaked index {Random_List[choice]}")
guess=int(input("guess the last element of the Random_list"))
if guess==Random_List[-1]:
    print(flag)
else:
    print("not today!")
