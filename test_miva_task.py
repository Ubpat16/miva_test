import pytest
from question_one import plus_one
from question_two import alter_min_max_rearrangement

def test_plus_one_example_one():
    input_digits = [1,2,3]
    output_digits = [1,2,4]
    
    assert plus_one(input_digits) == output_digits
    
def test_plus_one_example_two():
    input_digits = [4,3,2,1]
    output_digits = [4,3,2,2]

    assert plus_one(input_digits) == output_digits
    
def test_plus_one_example_three():
    input_digits = [9]
    output_digits = [1,0]

    assert plus_one(input_digits) == output_digits
    
def test_whole_numbers():
    input_digits = [5,9,9,9]
    output_digits = [6,0,0,0]
    
    assert plus_one(input_digits) == output_digits
    
def test_raise_constraint_violated_exception():
    input_digits = [0,9,9,9]

    with pytest.raises(ValueError):
        plus_one(input_digits)
    
def test_alternate_min_max_example_one():
    input_list = [13,7,8,3,2,10,15,-1]
    output_list = [-1, 15, 2, 13, 3, 10, 7, 8]

    assert alter_min_max_rearrangement(input_list) == output_list
    
def test_alternate_min_max_example_two():
    input_list = [-5, -12, -1, 7, 14, -7, 3, 6]
    output_list = [-12, 14, -7, 7, -5, 6, -1, 3]

    assert alter_min_max_rearrangement(input_list) == output_list
    
def test_alternate_min_max_example_three():
    input_list = [3, 6, 9, -10, -5, -2, 0, 8]
    output_list = [-10, 9, -5, 8, -2, 6, 0, 3]

    assert alter_min_max_rearrangement(input_list) == output_list
    
def test_alternate_min_max_custom_example():
    input_list = [0, 1, 2, 3, 4, 5, 6, 7]
    output_list = [0, 7, 1, 6, 2, 5, 3, 4]

    assert alter_min_max_rearrangement(input_list) == output_list
    
def test_contraint_violation():
    input_list = []
    with pytest.raises(ValueError):
        alter_min_max_rearrangement(input_list)
    
    input_list = ["4", "3", 1, 4]
    with pytest.raises(ValueError):
        alter_min_max_rearrangement(input_list)