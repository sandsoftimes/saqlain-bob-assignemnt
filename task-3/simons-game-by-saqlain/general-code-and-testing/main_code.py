from typing import TypeVar, List, Dict

T = TypeVar('T')

def reverse_list(items: List[T]) -> List[T]:
    return items[::-1]

def count_items(items: List[T]) -> Dict[T, int]:
    item_counts = {}
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1
    return item_counts


print("WELCOME-TO-THE-GAME-PLAYER :)")
value = int(input("How Many Numbers To START? Give Me A Number: "))
numbers = [] 

for i in range(0, value):
    vault = int(input("Enter " + str(i+1) + " Value: "))
    numbers.append(vault)  

reversed_numbers = reverse_list(numbers)
print("Reversed numbers:", reversed_numbers)

counts = count_items(numbers)
print("Item counts:", counts)

