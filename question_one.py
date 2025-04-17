from typing import List

def check_constraint(position: int, value: int, array_size: int) -> None:
    """
    Check if the given position and value violate any constraints.
    Returns False if constraints are violated, True otherwise.
    """
    
    if array_size < 1 or array_size > 100:
        # 1 <= digits.length <= 100
        raise ValueError("Invalid input: Array size out of range")

    if value < 0 or value > 9:
        # 0 <= digits[i] <= 9
        raise ValueError("Invalid input: Value out of range")
    
    if position == 0 and array_size > 1 and value == 0:
        # leading zeros not allowed
        raise ValueError("Invalid input: Leading zeros not allowed")
    
    return
    
def validate_constraints(digits_array: List[str]) -> List[str]:
    """
    Validate all constraints for the input digits.
    Returns True if all constraints are satisfied, False otherwise.
    """
    
    for index, value in enumerate(digits_array):
        check_constraint(index, value, len(digits_array))
    
    return

def to_digits_array(digits: int):
    """
    Convert an integer to a list of digits.
    """
    return list(map(int, str(digits)))

def plus_one(digits_array: List[int]) -> List[int]:
    """
    Increment the large integer represented by the input digits by one and return the result.
    """
    validate_constraints(digits_array)
    joined_array = "".join(map(str, digits_array))
    int_joined_array = int(joined_array)
    if digits_array[-1] < 9:
        # first simple case where we are just increase the digt[-1] by 1
        int_joined_array += 1
        return to_digits_array(int_joined_array)
    
    int_joined_array += 1
    return to_digits_array(int_joined_array)