import heapq
import random
from typing import List, Tuple

def minimize_cost(cable_lengths: List[int]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """
    Minimize the total cost of connecting cables and provide the plan.
    Args:
        cable_lengths: list[int] - list of cable lengths
    Returns:
        Tuple[int, List[Tuple[int, int, int]]]: 
            - minimum total cost
            - list of tuples representing the plan (a, b, cost)
    """
    if not cable_lengths:
        return 0, []
    if len(cable_lengths) == 1:
        return 0, []

    heap = list(cable_lengths)    
    heapq.heapify(heap)
    total = 0
    # Plan to keep track of the merging process
    plan: List[Tuple[int, int, int]] = []

    while len(heap) > 1:
        # get first and second minimum lengths
        first_min = heapq.heappop(heap)
        second_min = heapq.heappop(heap)
        # merge them
        merged = first_min + second_min
        total += merged
        # record the operation in the plan
        plan.append((first_min, second_min, merged))
        # push the merged cable back to the heap
        heapq.heappush(heap, merged)

    return total, plan

# Example usage:
if __name__ == "__main__":
    cable_lengths =  [random.randint(1, 10) for _ in range(6)]
    total_cost, plan = minimize_cost(cable_lengths)
    print()
    print(f"Cable lengths: {cable_lengths}")
    print("Plan (a + b -> cost):", " -> ".join(f"({a}+{b}={c})" for a,b,c in plan))
    print(f"Minimum total cost: {total_cost}\n")
