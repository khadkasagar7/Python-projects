# randomisation and python list

import random

friend = ["カドカ", "仲田", "高橋","中山"]

# 1 option
print(random.choice(friend))

# 2 option
random_index = random.randint(0,3)
print(friend[random_index])