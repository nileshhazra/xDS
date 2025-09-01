import heapq
from typing import List


def maxAverageRatio(classes: List[List[int]], extraStudents: int):
    # Set this True to print heap state step-by-step for learning
    DEBUG = True

    def gain(p: int, t: int) -> float:
        # marginal gain when adding one student to (p, t)
        return (t - p) / (t * (t + 1))

    n = len(classes)
    heap = []  # we will store tuples: ( -gain, p, t )

    # Build the heap with initial gains
    for p, t in classes:
        g = gain(p, t)
        # We push negative gain because heapq is a min-heap.
        heapq.heappush(heap, (-g, p, t))

    if DEBUG:
        print("Initial heap (neg_gain, p, t):")
        print(heap)

    # Assign each extra student greedily
    for i in range(extraStudents):
        neg_g, p, t = heapq.heappop(heap)  # get class with max gain (smallest neg_g)
        # DEBUG print
        if DEBUG:
            print(f"\nStep {i+1}: popped (neg_gain={neg_g:.8f}, p={p}, t={t})")

        # assign one brilliant student
        p += 1
        t += 1

        # recompute gain and push back
        new_g = gain(p, t)
        heapq.heappush(heap, (-new_g, p, t))

        if DEBUG:
            print(f"Pushed updated (neg_gain={-new_g:.8f}, p={p}, t={t})")
            print("Heap now:")
            print(heap)

    # After assignments, sum final ratios
    total = 0.0
    while heap:
        _, p, t = heapq.heappop(heap)
        total += p / t

    return total / n


maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 2)
