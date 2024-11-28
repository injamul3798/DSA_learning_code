import heapq

# Create a list to represent a heap
min_heap = []

# Insert elements into the heap
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 6)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 4)

print("Min Heap:", min_heap)  # Min Heap: [1, 2, 4, 5, 3, 6]

# Extract the minimum element
min_element = heapq.heappop(min_heap)
print("Extracted Minimum:", min_element)  # Extracted Minimum: 1
print("Min Heap after extraction:", min_heap)  # [2, 3, 4, 5, 6]




# MaxHeap 
# ------------------------------------------

# Create a list to represent a heap
max_heap = []

# Insert elements into the heap (negate the values to simulate max heap)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -6)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -4)

# Convert back to positive values to view the heap as a max-heap
print("Max Heap:", [-x for x in max_heap])  # Max Heap: [6, 5, 4, 1, 2, 3]

# Extract the maximum element
max_element = -heapq.heappop(max_heap)  # Negate back to get the original value
print("Extracted Maximum:", max_element)  # Extracted Maximum: 6

# Convert back to positive values to view the heap after extraction
print("Max Heap after extraction:", [-x for x in max_heap])  # [5, 3, 4, 1, 2]
