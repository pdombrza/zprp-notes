import heapq

nums = [1, 8, 2, -4, 5, -7, 22, 33, 4, 38]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "GOOGL", "shares": 76, "price": 543.2},
    {"name": "FB", "shares": 42, "price": 73.2},
    {"name": "ACME", "shares": 167, "price": 143.65},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s["price"])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s["price"])

print(cheap)
print(expensive)