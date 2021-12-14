import Tools
import aocd
from collections import Counter, defaultdict, deque
from functools import cache

with open('inputs/session.txt') as f:
    session = f.read()

timer = Tools.Timer()
data = aocd.get_data(session, day=1)

timer.stop()
