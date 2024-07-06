# Import the time library
import time

# How many times to run each function
ITERATIONS = 10_000_000


def add_arr():
    """Add item to beginning of list using list concatenation."""
    arr = [1, 2, 3, 4, 5]
    return [0] + arr


def insert_arr():
    """Add item to beginning of list using insert method."""
    arr = [1, 2, 3, 4, 5]
    arr.insert(0, 0)
    return arr


# https://stackoverflow.com/questions/1720421/how-do-i-concatenate-two-lists-in-python
def unpacking_arr():
    """Add item to beginning of list using unpacking."""
    arr = [1, 2, 3, 4, 5]
    return [0, *arr]


def add_loop():
    """Loop for running add_arr() function."""
    start = time.time()
    for i in range(ITERATIONS):
        add_arr()
    end = time.time()
    total = end - start
    print(f"add_arr() -> {total} seconds for {'{:,}'.format(ITERATIONS)} loops")


def insert_loop():
    """Loop for running insert_arr() function."""
    start = time.time()
    for i in range(ITERATIONS):
        insert_arr()
    end = time.time()
    total = end - start
    print(f"insert_arr() -> {total} seconds for {'{:,}'.format(ITERATIONS)} loops")


def unpacking_loop():
    """Loop for running unpacking_arr() function."""
    start = time.time()
    for i in range(ITERATIONS):
        unpacking_arr()
    end = time.time()
    total = end - start
    print(f"unpacking_arr() -> {total} seconds for {'{:,}'.format(ITERATIONS)} loops")


# Fastest
insert_loop()
# Second Fastest
add_loop()
# Slowest
unpacking_loop()
