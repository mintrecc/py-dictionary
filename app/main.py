from dataclasses import dataclass


@dataclass
class Node:
    key: str | int
    hashed: int
    value: str | int


class Dictionary:
    def __init__(self) -> None:
        self.hash_table = [None] * 8
        self.counter = 0

    def __len__(self) -> int:
        return self.counter

    def _resize(self) -> None:

        temp_list = self.hash_table
        new_size = len(self.hash_table) * 2

        self.hash_table = [None] * new_size

        for item in temp_list:
            if item is not None:
                index = item.hashed % new_size

                while self.hash_table[index] is not None:
                    index = (index + 1) % new_size

                self.hash_table[index] = item

    def __setitem__(self, key: int | str, value: int | str) -> None:

        if self.counter > (len(self.hash_table) * 2 / 3):
            self._resize()

        item_to_add = Node(key, hash(key), value)
        index = hash(key) % len(self.hash_table)

        while True:

            if self.hash_table[index] is None:
                self.counter += 1
                self.hash_table[index] = item_to_add
                break

            if (self.hash_table[index] is not None
                    and self.hash_table[index].key == key):
                self.hash_table[index] = item_to_add
                break

            elif (self.hash_table[index] is not None
                  and self.hash_table[index].key != key):
                index = (index + 1) % len(self.hash_table)

    def __getitem__(self, key: int | str) -> int | str:
        for item in self.hash_table:
            if item is not None and item.key == key:
                return item.value
        else:
            raise KeyError
