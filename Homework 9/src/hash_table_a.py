"""hash_table_a.py

For Q2a.
"""

from typing import Any, Generator, Iterator, Optional


class Node:
    def __init__(self, val: Any) -> None:
        self.value: Any = val
        self.next: Optional["Node"] = None


class HashTable:
    def __init__(self, buckets: int) -> None:
        self.array: list[Node | None] = [None] * buckets

    def insert(self, val: Any) -> None:
        bucket = hash(val) % len(self.array)
        tmp_head = Node(val)
        tmp_head.next = self.array[bucket]
        self.array[bucket] = tmp_head

    def __iter__(self) -> Iterator:
        def hash_table_generator() -> Generator:
            for head in self.array:
                while head is not None:
                    yield head.value
                    head = head.next
        return hash_table_generator()


table = HashTable(5)
for num in range(20):
    table.insert(num)

# You can check by piping output into `sort -n` and `wc -l`.
for value in table:
    print(value)

print()

iterator = table.__iter__()
while True:
    try:
        value = iterator.__next__()
        print(value)
    except StopIteration:
        break
