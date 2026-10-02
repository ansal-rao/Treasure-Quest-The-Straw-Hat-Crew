from straw_hat import StrawHatTreasury
from treasure import Treasure

s = StrawHatTreasury(2)
t1 = Treasure(2001, 10, 1)
t2 = Treasure(2002, 15, 1)
t3 = Treasure(2003, 20, 15)
s.add_treasure(t1)
s.add_treasure(t2)
s.add_treasure(t3)
treasure_list = s.get_completion_time()

# Expected completion times
expected_completion_times = [11, 16, 35]

# Get actual completion times
actual_completion_times = [treasure.completion_time for treasure in treasure_list]

# Check if the actual completion times match the expected completion times
if actual_completion_times == expected_completion_times:
    print("Test Passed")
else:
    print("Test Failed")
    print(f"Expected: {expected_completion_times}")
    print(f"Actual: {actual_completion_times}")