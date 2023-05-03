# James Pham, 1823491
# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    # Pick the middle element as pivot
    pivot_index = (i + k) // 2
    pivot_value = user_ids[pivot_index]

    # Initialize low and high indices
    l = i
    h = k

    # Partition loop
    while True:
        # Find the next element on the left that should be on the right
        while user_ids[l] < pivot_value:
            l += 1

        # Find the next element on the right that should be on the left
        while user_ids[h] > pivot_value:
            h -= 1

        # If low and high indices have crossed, the partition is complete
        if l >= h:
            return h

        # Swap the left and right elements
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]

        # Move to the next elements on each side
        l += 1
        h -= 1


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quicksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1

    if i < k:
        # Partition the array
        j = partition(user_ids, i, k)

        # Recursively sort the left and right partitions
        quicksort(user_ids, i, j)
        quicksort(user_ids, j + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
