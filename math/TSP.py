# TSP comparison: Brute Force vs Held–Karp vs Nearest Neighbor vs Simulated Annealing
# Generates a small random TSP instance (10 cities), solves with four methods,
# compares tour cost and runtime, and plots the resulting tours.
import math, itertools, time, random, os
from dataclasses import dataclass
from typing import List, Tuple, Dict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# For nice reproducibility
random.seed(42)
np.random.seed(42)

# ---------------------------
# Problem instance
# ---------------------------
N = 13  # number of cities (10 keeps brute force manageable: 9! ≈ 362k tours)
coords = np.random.rand(N, 2) * 100.0  # random 2D coordinates in [0,100)
# Euclidean distance matrix
def euclid(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])
dist = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        dist[i, j] = 0.0 if i == j else euclid(coords[i], coords[j])

def tour_length(tour: List[int]) -> float:
    s = 0.0
    for i in range(len(tour)-1):
        s += dist[tour[i], tour[i+1]]
    s += dist[tour[-1], tour[0]]  # return to start
    return s

# ---------------------------
# 1) Brute Force (exact, factorial)
# ---------------------------
def brute_force_tsp() -> Tuple[List[int], float]:
    start = 0
    others = list(range(1, N))
    best_cost = float('inf')
    best_tour = None
    for perm in itertools.permutations(others):
        tour = [start] + list(perm)
        c = tour_length(tour)
        if c < best_cost:
            best_cost = c
            best_tour = tour
    return best_tour, best_cost

# ---------------------------
# 2) Held–Karp DP (exact, O(n^2 2^n))
# ---------------------------
def held_karp(dist_matrix: np.ndarray) -> Tuple[List[int], float]:
    n = dist_matrix.shape[0]
    # DP[(S, j)] = (cost, prev) where S is a bitmask including 0 and j
    # S does not include the start's bit explicitly in transitions, but we enforce start=0.
    DP: Dict[Tuple[int, int], Tuple[float, int]] = {}
    # Initialize: paths starting from 0 to j
    for j in range(1, n):
        DP[(1 << j, j)] = (dist_matrix[0, j], 0)
    # Iterate subsets of increasing size
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # bitmask of subset
            bits = 0
            for b in subset:
                bits |= 1 << b
            for j in subset:
                prev_bits = bits & ~(1 << j)
                best = (float('inf'), -1)
                for k in subset:
                    if k == j: 
                        continue
                    prev_cost, _ = DP[(prev_bits, k)]
                    cost = prev_cost + dist_matrix[k, j]
                    if cost < best[0]:
                        best = (cost, k)
                DP[(bits, j)] = best
    # Close the tour back to 0
    bits_all = 0
    for m in range(1, n):
        bits_all |= 1 << m
    best_cost = float('inf')
    last = -1
    for j in range(1, n):
        cost, _ = DP[(bits_all, j)]
        cost += dist_matrix[j, 0]
        if cost < best_cost:
            best_cost = cost
            last = j
    # Reconstruct path
    tour = [0]
    bits = bits_all
    j = last
    for _ in range(n-1):
        tour.append(j)
        cost, prev = DP[(bits, j)]
        bits &= ~(1 << j)
        j = prev
    return tour, best_cost

# ---------------------------
# Run all methods & time them
# ---------------------------
results = []

# Brute Force
t0 = time.perf_counter()
bf_tour, bf_cost = brute_force_tsp()
t1 = time.perf_counter()
results.append(("Brute Force (Exact)", bf_cost, t1 - t0, bf_tour))

# Held–Karp
t0 = time.perf_counter()
hk_tour, hk_cost = held_karp(dist)
t1 = time.perf_counter()
results.append(("Held–Karp (Exact)", hk_cost, t1 - t0, hk_tour))

# ---------------------------
# Summarize results
# ---------------------------
df = pd.DataFrame({
    "Método": [r[0] for r in results],
    "Costo de la gira": [r[1] for r in results],
    "Tiempo (s)": [r[2] for r in results],
    "Tour": [r[3] for r in results],
}).sort_values(by="Costo de la gira").reset_index(drop=True)


print(df)