route = [
    "You stand at a crossroads. The path to the left is dark and mysterious, the path to the right is bright and inviting, and straight ahead, a narrow path winds into the distance. Which way will you go: left(l), right(r), or straight(s)?",
    "You reach a fork in the road. The left path leads into a dense forest, the right path leads to a sparkling river, and straight ahead, a steep mountain path beckons. Which way will you go: left(l), right(r), or straight(s)?",
    "You find yourself at a three-way junction. The left path is overgrown with vines, the right path is paved with cobblestones, and the path straight ahead disappears into a thick fog. Which way will you go: left(l), right(r), or straight(s)?",
    "A hidden passageway splits into three. The left passage is filled with the sound of dripping water, the right passage is silent, and the straight passage is dimly lit. Which way will you go: left(l), right(r), or straight(s)?",
    "You encounter a strange crossroads. The left path is marked with a symbol of the moon, the right path with a symbol of the sun, and the straight path with a symbol of the stars. Which path will you choose: left(l), right(r), or straight(s)?"
]
   
print(route[0])

adventure_questions = [
    {'question': 'What is the output of the following code? print("Hello, world!")','answer': ['hello, world!']},
    # {'question': 'What is this [1, 2, 3, "apple", "banana"] a dictionary or a list?', 'answer': ['list']},
    # {'question': 'Is it possible to change elements in tupl after creation?', 'answer': ['no']},
    # {'question': 'What word defines the function?', 'answer': ['def']},
    # {'question': 'What function generates a sequence of numbers', 'answer': ['range', 'range()']},
    # {'question': 'What is the data type of the value 3.14?', 'answer': ['float']},
    # {'question': 'What is the output of 2 ** 3?', 'answer': ['8']},
    # {'question': 'How do you create an empty list (use as list name "list1")?', 'answer': ["list1 = []"]},
    # {'question': 'How do you access the third element in a list named "my_list"?', 'answer': ['my_list[2]']},
    # {'question': 'How do you add an element to a set (use my_set, element)?', 'answer': ['my_set.add(element)']},
    # {'question': 'What is the purpose of the "try-except" block?', 'answer': ['To handle exceptions', 'handle exceptions']},
    # {'question': 'What is the output of "len(None)?"', 'answer': ['TypeError']},
    # {'question': 'How do you create a class in Python? (use as classname MyClass)', 'answer': ['class MyClass:', 'class MyClass']},
    # {'question': 'What is a lambda function?', 'answer': ['A small, anonymous function', 'anonymous function']},
    # {'question': 'How do you import a module in Python? (use module_name)', 'answer': ['import module_name']},
    # {'question': 'What is the output of: `print(len("hello"))`?', 'answer': ['5']},
    # {'question': 'What is the output of: `print(list(range(5)))`?', 'answer': ['[0, 1, 2, 3, 4]']},
    # {'question': 'What is the output of: `print("hello"[2])`?', 'answer': ['l']},
    # {'question': 'What is the output of: `print(not True)`?', 'answer': ['False']},
    # {'question': 'What is the output of: `print(3 ** 3)`?', 'answer': ['27']},
    # {'question': 'What is the output of: `print(10 // 3)`?', 'answer': ['3']},
    # {'question': 'What is the output of: `print(10 % 3)`?', 'answer': ['1']},
    # {'question': 'What is the output of: `print("hello" * 3)`?', 'answer': ['hellohellohello']},
    # {'question': 'What is the output of: `my_list = [1, 2, 3]; my_list.append(4); print(my_list)`?', 'answer': ['[1, 2, 3, 4]']},
    # {'question': 'What is the output of: `my_dict = {"name": "Alice", "age": 30}; print(my_dict["name"])`?', 'answer': ['Alice']},
    # {'question': 'What is the output of: `def greet(name): print("Hello,", name + "!"); greet("Bob")`?', 'answer': ['Hello, Bob!']},
    # {'question': 'What is the output of: `numbers = [1, 2, 3, 4, 5]; squared = list(map(lambda x: x**2, numbers)); print(squared)`?', 'answer': ['[1, 4, 9, 16, 25]']},
    # {'question': 'What is the output of: `my_list = [1, 2, 3, 4, 5]; new_list = [x for x in my_list if x > 2]; print(new_list)`?', 'answer': ['[3, 4, 5]']},
    # {'question': 'What is the output of: `import math; print(math.sqrt(16))`?', 'answer': ['4.0']},
    # {'question': 'What is the output of: `my_set = {1, 2, 3, 2}; print(my_set)`?', 'answer': ['{1, 2, 3}']},
    # {'question': 'What is the output of: `try: 10 / 0 except ZeroDivisionError: print("Division by zero")`?', 'answer': ['Division by zero']},
    # {'question': 'What is the output of: `my_tuple = (1, 2, 3); print(my_tuple[1])`?', 'answer': ['2']},
    # {'question': 'What is the output of: `my_string = "hello"; print(my_string.upper())`?', 'answer': ['HELLO']},
    # {'question': 'What is the output of: `my_list = [1, 2, 3]; my_list.reverse(); print(my_list)`?', 'answer': ['[3, 2, 1]']},
    # {'question': 'What is the output of: `import numpy as np; arr = np.array([1, 2, 3]); print(arr.mean())`?', 'answer': ['2.0']},
    # {'question': 'What is the output of: `my_list = [1, 2, 3]; del my_list[1]; print(my_list)`?', 'answer': ['[1, 3]']},
    # {'question': 'What is the output of: `name = "Alice"; print(f"Hello, {name}!")`?', 'answer': ['Hello, Alice!']},
    # {'question': 'What is the output of: `my_string = "apple"; print(my_string.count("p"))`?', 'answer': ['2']},
    # {'question': 'What is the output of: `x = 10; y = 5; print(x if x > y else y)`?', 'answer': ['10']},
    # {'question': 'What is the output of: `def sum_of_squares(numbers): return sum(x**2 for x in numbers); print(sum_of_squares([1, 2, 3]))`?', 'answer': ['14']},
    # {'question': 'What is the output of: `my_list = [1, "apple", 3.14]; print(my_list[1])`?', 'answer': ['apple']},
    # {'question': 'What is the output of: `try: int("hello") except ValueError: print("Invalid input")`?', 'answer': ['Invalid input']},
    # {'question': 'What is the output of: `my_list = [1, 2, 3, 4]; print(my_list.index(2))`?', 'answer': ['1']},
    # {'question': 'What is the output of: `my_string = "banana"; print(my_string.replace("a", "e"))`?', 'answer': ['benene']},
    # {'question': 'What is the output of: `class Animal: def __init__(self, name): self.name = name; animal1 = Animal("Dog"); print(animal1.name)`?', 'answer': ['Dog']},
    # {'question': 'What is the output of: `def is_even(number): return number % 2 == 0; print(is_even(7))`?', 'answer': ['False']},
    # {'question': 'What is the output of: `my_list = [10, 20, 30]; newList = sorted(my_list, reverse=True); print(newList)`?', 'answer': ['[30, 20, 10]']},
    # {'question': 'What is the output of: `my_tuple = (1, 2, 3); print(my_tuple + (4, 5))`?', 'answer': ['(1, 2, 3, 4, 5)']},
    # {'question': 'What is the output of: `my_string = "hello world"; print(my_string.split())`?', 'answer': ['["hello", "world"]']},

]