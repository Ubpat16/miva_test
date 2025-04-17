from typing import List


def check_constraint(integer_array: List[int]) -> bool:
    # Array consist list of integers
    # Array can not be empty
    # Elements in the array can be positive, negative or zero
    
    if not all(isinstance(x, int) for x in integer_array):
        raise ValueError("Array should consist only integers")
    
    if not integer_array:
        raise ValueError("Array can not be empty")
    
    return

def get_min_value_from_the_array(integer_array: List[int]) -> int:
    return min(integer_array)

def get_max_value_from_the_array(integer_array: List[int]) -> int:
    return max(integer_array)

def alter_min_max_rearrangement(integer_array: List[int]) -> List[int]:
    check_constraint(integer_array)
    
    # idea is to get the min and max from the array then remove then min and max value from the array
    # append them a new array then repeat the process untill there is no longer an element in the old array
    
    new_array = []
    while len(integer_array) > 1:
        min_value = get_min_value_from_the_array(integer_array)
        max_value = get_max_value_from_the_array(integer_array)

        integer_array.remove(min_value)
        integer_array.remove(max_value)

        new_array.append(min_value)
        new_array.append(max_value)
    return new_array
