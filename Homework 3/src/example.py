#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""example.py

Python code to test my answers for this assignment.

USAGE: ./example.py
"""

from functools import partial, reduce
from io import StringIO
from typing import Any, Callable

__author__ = "Vincent Lin"


def question1() -> None:
    def convert_to_decimal(bits: list[int]) -> int:
        exponents = range(len(bits)-1, -1, -1)
        nums = [bit * 2**exponent for bit, exponent in zip(bits, exponents)]
        return reduce(lambda acc, num: acc + num, nums)
    assert convert_to_decimal([1, 0, 1, 1, 0]) == 22
    assert convert_to_decimal([1, 0, 1]) == 5


def question2() -> None:
    def parse_csv(lines: list[str]) -> list[tuple[str, int]]:
        return [(string, int(num)) for string, num in [
            line.split(",") for line in lines
        ]]

    assert parse_csv(["apple,8", "pear,24", "gooseberry,-2"]) == \
        [("apple", 8), ("pear", 24), ("gooseberry", -2)]

    def unique_characters(sentence: str) -> set[str]:
        return {char for char in sentence}

    assert unique_characters("happy") == {"h", "a", "p", "y"}

    def squares_dict(lower_bound: int, upper_bound: int) -> dict[int, int]:
        return {num: num**2 for num in range(lower_bound, upper_bound+1)}

    assert squares_dict(1, 5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def question3() -> None:
    def strip_characters(sentence: str, chars_to_remove: set[str]) -> str:
        return "".join(char for char in sentence
                       if char not in chars_to_remove)

    assert strip_characters("Hello, world!", {"o", "h", "l"}) == "He, wrd!"


def question4() -> None:
    class Box:
        def __init__(self, value):
            self.value = value
    def quintuple(num):
        num *= 5
    def box_quintuple(box):
        box.value *= 5
        num = 3
        box = Box(3)

    num = 3
    box = Box(3)

    quintuple(num)
    box_quintuple(box)
    # 3 15
    # print(f"{num} {box.value}")


def question6() -> None:
    class Duck:
        def __init__(self) -> None:
            pass  # Empty initializer
    class DuckPretender:
        def quack(self) -> None:
            pass  # Doesn't need to do anything
    class MallardDuck(Duck):
        pass

    def is_duck_a(duck: Any) -> bool:
        try:
            duck.quack()
            return True
        except:
            return False
    def is_duck_b(duck: Any) -> bool:
        return isinstance(duck, Duck)

    duck = DuckPretender()
    mallard = MallardDuck()
    assert is_duck_a(duck) is True
    assert is_duck_b(duck) is False
    assert is_duck_a(mallard) is False
    assert is_duck_b(mallard) is True


def question7() -> None:
    def largest_sum(nums, k):  # type: ignore
        if k < 0 or k > len(nums):
            raise ValueError
        elif k == 0:
            return 0
        max_sum = None
        for i in range(len(nums)-k+1):
            sum = 0
            for num in (nums[j] for j in range(i,i+k)):
                sum += num
            if max_sum is None or sum > max_sum:
                max_sum = sum
        return max_sum

    assert largest_sum([3,5,6,2,3,4,5], 3) == 14
    assert largest_sum([10,-8,2,6,-1,2], 4) == 10

    def largest_sum(nums, k):
        if k < 0 or k > len(nums):
            raise ValueError
        elif k == 0:
            return 0
        sum = 0
        # First find the sum of the first k elements.
        for num in (nums[j] for j in range(k)):
            sum += num
        max_sum = sum
        # Now we apply the sliding window technique.
        for i in range(0, len(nums)-k-1):
            sum -= nums[i]
            sum += nums[i+k]
            max_sum = max(sum, max_sum)
        return max_sum

    assert largest_sum([3,5,6,2,3,4,5], 3) == 14
    assert largest_sum([10,-8,2,6,-1,2], 4) == 10


def question8() -> None:
    class Event:
        def __init__(self, start_time: int, end_time: int) -> None:
            if start_time >= end_time:
                raise ValueError
            self.start_time = start_time
            self.end_time = end_time

    def test_event() -> str:
        output = StringIO()
        test_print = partial(print, file=output)

        event = Event(10, 20)
        test_print(f"Start: {event.start_time}, End: {event.end_time}")
        try:
            invalid_event = Event(20, 10)
            test_print("Success")
        except ValueError:
            test_print("Created an invalid event")

        return output.getvalue()

    assert test_event() == "Start: 10, End: 20\nCreated an invalid event\n"

    class Calendar:
        def __init__(self) -> None:
            self.__events: list[Event] = []

        def get_events(self) -> list[Event]:
            return self.__events

        def add_event(self, event: Any) -> None:
            if not isinstance(event, Event):
                raise TypeError
            self.__events.append(event)

    def test_calendar() -> str:
        output = StringIO()
        test_print = partial(print, file=output)

        calendar = Calendar()
        test_print(calendar.get_events())
        calendar.add_event(Event(10, 20))
        test_print(calendar.get_events()[0].start_time)
        try:
            calendar.add_event("not an event")
        except TypeError:
            test_print("Invalid event")

        return output.getvalue()

    assert test_calendar() == "[]\n10\nInvalid event\n"

    # Solution 1
    class AdventCalendar(Calendar):  # type: ignore
        def __init__(self, year: int) -> None:
            super().__init__()  # Added this line.
            self.year = year

    advent_calendar = AdventCalendar(2022)
    assert advent_calendar.get_events() == []

    class AdventCalendar(Calendar):
        def __init__(self, year):
            self.year = year
            self.__events: list[Event] = []  # Added this line.
        # Added this method.
        def get_events(self) -> list[Event]:
            return self.__events

    advent_calendar = AdventCalendar(2022)
    assert advent_calendar.get_events() == []


def question9() -> None:
    def outer_function(x: int) -> Callable[[int], int]:
        def inner_function(y: int) -> int:
            return x + y
        return inner_function

    add_6 = outer_function(6)
    assert add_6(15) == 21


def main() -> None:
    question1()
    question2()
    question3()
    question4()
    question6()
    question7()
    question8()
    question9()


if __name__ == "__main__":
    main()
