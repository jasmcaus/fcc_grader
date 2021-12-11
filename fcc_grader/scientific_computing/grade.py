from ..core import _grade 

def grade_lesson1(result):
    _grade("scientific-computing", "lesson1", str(result))

def grade_lesson2(result):
    _grade("scientific-computing", "lesson2", result.tolist())

def grade_lesson3(result):
    _grade("scientific-computing", "lesson3", result)