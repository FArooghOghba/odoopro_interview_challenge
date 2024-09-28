from typing import List
from unittest import TestCase


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers `nums` and an integer `target`,
    return the indices of the two numbers such that they
    add up to the target.

    This function uses a hash map (dictionary) to store indices of
    previously seen numbers, allowing for constant time lookups.
    This results in an efficient O(n) time complexity as each element
    is processed at most once.

    Args:
        nums (List[int]): List of integers to search through.
        target (int): Target sum to find.

    Returns:
        List[int]: A list containing the indices of the two numbers
        that add up to the target.
    """

    indices = {}

    for index, num in enumerate(nums):
        other_num = target - num
        if other_num in indices:
            return [indices[other_num], index]

        indices[num] = index

    return []


class TestTwoSum(TestCase):

    """
    Test cases for the `two_sum` function to ensure correct
    behavior under various conditions such as standard cases,
    edge cases, and error handling.
    """

    def test_standard_case(self) -> None:

        """
        Test a standard case where a valid pair of numbers exists
        that adds up to the target.
        Example: nums=[2, 7, 11, 15], target=9.
        """

        result = two_sum(nums=[2, 7, 11, 15], target=9)
        self.assertEqual(first=set(result), second={0, 1})

    def test_no_solution(self) -> None:

        """
        Test the case where no pair of numbers adds up to the target.
        Example: nums=[2, 7, 11, 15], target=50.
        """

        result = two_sum(nums=[2, 7, 11, 15], target=50)
        self.assertEqual(first=result, second=[])

    def test_duplicate_numbers(self) -> None:

        """
        Test the case where the list contains duplicate numbers
        that sum to the target.
        Example: nums=[3, 3], target=6.
        """

        result = two_sum(nums=[3, 3], target=6)
        self.assertEqual(first=set(result), second={0, 1})

    def test_same_number_used_twice(self) -> None:

        """
        Test the case where the same number cannot be used twice
        to meet the target.
        Example: nums=[3, 2, 4], target=6.
        """

        result = two_sum(nums=[3, 2, 4], target=6)
        self.assertEqual(first=set(result), second={1, 2})

    def test_empty_list(self) -> None:

        """
        Test the case where the input list is empty.
        Example: nums=[], target=9.
        """

        result = two_sum(nums=[], target=9)
        self.assertEqual(first=result, second=[])

    def test_single_number(self) -> None:

        """
        Test the case where the list contains only one number.
        Example: nums=[7], target=9.
        """

        result = two_sum(nums=[7], target=9)
        self.assertEqual(first=result, second=[])
