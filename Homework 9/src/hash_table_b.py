"""hash_table_b.py

For Q2b and 2e.
"""

from typing import Any, Callable, Iterator, Optional


class Node:
    def __init__(self, val: Any) -> None:
        self.value: Any = val
        self.next: Optional["Node"] = None


class HashTableIterator:
    def __init__(self, array: list[Node | None]) -> None:
        self.array = array
        self.bucket = -1
        self.node: Node | None = None
        # Set initial node to the head of the first non-None list.
        self._set_to_next_bucket()

    def _set_to_next_bucket(self) -> None:
        for i in range(self.bucket + 1, len(self.array)):
            if self.array[i] is not None:
                self.bucket = i
                self.node = self.array[i]
                break

    def __next__(self) -> Any:
        # Attempt to move on to the next bucket.
        if self.node is None:
            self._set_to_next_bucket()
        # No more buckets left.
        if self.node is None:
            raise StopIteration
        # Return the current value and advance the current list.
        value = self.node.value
        self.node = self.node.next
        return value

    def __iter__(self) -> Iterator:
        return self


class HashTable:
    def __init__(self, buckets: int) -> None:
        self.array: list[Node | None] = [None] * buckets

    def insert(self, val: Any) -> None:
        bucket = hash(val) % len(self.array)
        tmp_head = Node(val)
        tmp_head.next = self.array[bucket]
        self.array[bucket] = tmp_head

    def __iter__(self) -> Iterator:
        return HashTableIterator(self.array)

    def forEach(self, callback: Callable[[Any], Any]) -> None:
        for head in self.array:
            if head is None:
                continue
            current = head
            while current is not None:
                callback(current.value)
                current = current.next


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

print()

table.forEach(lambda x: print(x))
