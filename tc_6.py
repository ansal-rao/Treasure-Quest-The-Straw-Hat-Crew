from treasure import Treasure
from straw_hat import StrawHatTreasury

s = StrawHatTreasury(2)
t1 = Treasure(2001, 10, 1)
t2 = Treasure(2002, 15, 1)
t3 = Treasure(2003, 4, 4)
s.add_treasure(t1)
s.add_treasure(t2)
s.add_treasure(t3)
completed_treasures = s.get_completion_time()
for treasure in completed_treasures:
    print(treasure.id, treasure.completion_time)

print()

s2 = StrawHatTreasury(2)
t21 = Treasure(2003, 10, 1)
t22 = Treasure(2002, 15, 1)
t23 = Treasure(2001, 4, 4)
s2.add_treasure(t21)
s2.add_treasure(t22)
s2.add_treasure(t23)
completed_treasures_2 = s2.get_completion_time()
for treasure in completed_treasures_2:
    print(treasure.id, treasure.completion_time)