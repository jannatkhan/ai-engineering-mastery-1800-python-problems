Day 5 – Python List Coding Interview Programs (81–100)
Today’s topic: Python Lists – Most Frequently Asked Technical Interview Questions.
Lists are one of the most important Python topics. Interviewers use list questions to test loops, indexing, sorting, searching, dictionaries and problem-solving skills.
Part 1: Basic list programs 81. Find the largest element in a list
numbers = [10, 25, 5, 80, 45]

largest = numbers[0]

for num in numbers:
if num > largest:
largest = num

print(largest)
Output:
80
Explanation:

- Assume the first element is the largest.
- Compare every element.
- Update the largest value whenever a bigger number is found.
  Time complexity: O(n).

82. Find the smallest element in a list
    numbers = [10, 25, 5, 80, 45]

smallest = numbers[0]

for num in numbers:
if num < smallest:
smallest = num

print(smallest)
Output: 5 83. Find the second largest element without sorting
numbers = [10, 20, 40, 30, 50]

first = second = float('-inf')

for num in numbers:
if num > first:
second = first
first = num
elif num > second and num != first:
second = num

print(second)
Output: 40
Explanation: Maintain two variables for the largest and second-largest distinct values.
Time complexity: O(n). 84. Find the sum of all list elements
numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
total += num

print(total)
Output: 100 85. Find the average of list elements
numbers = [10, 20, 30, 40]

average = sum(numbers) / len(numbers)

print(average)
Output: 25.0 86. Reverse a list without using reverse()
numbers = [1, 2, 3, 4, 5]

result = []

for num in numbers:
result.insert(0, num)

print(result)
Output:
[5, 4, 3, 2, 1]
Explanation: Insert every element at index zero.
Note: This approach takes O(n²) time because inserting at the beginning shifts existing elements. 87. Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in numbers:
if num not in result:
result.append(num)

print(result)
Output:
[1, 2, 3, 4, 5]
Explanation: Keep an element only if it has not appeared before. 88. Count even and odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for num in numbers:
if num % 2 == 0:
even += 1
else:
odd += 1

print("Even:", even)
print("Odd:", odd)
Output:
Even: 3
Odd: 3 89. Find duplicate elements in a list
numbers = [1, 2, 3, 2, 4, 5, 3]

seen = set()
duplicates = set()

for num in numbers:
if num in seen:
duplicates.add(num)
else:
seen.add(num)

print(sorted(duplicates))
Output:
[2, 3]
Explanation: Use a set to track previously visited elements.
Time complexity: O(n) average. 90. Find the frequency of each element
numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in numbers:
frequency[num] = frequency.get(num, 0) + 1

print(frequency)
Output:
{1: 1, 2: 2, 3: 3, 4: 1}
Part 2: Important list interview problems 91. Move all zeros to the end
numbers = [0, 1, 0, 3, 12]

result = [num for num in numbers if num != 0]

result += [0] \* (len(numbers) - len(result))

print(result)
Output:
[1, 3, 12, 0, 0]
Explanation:

- Collect all non-zero elements.
- Append the required number of zeros.
- Original non-zero order is preserved.
  Time complexity: O(n).

92. Find common elements between two lists
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]

result = list(set(a) & set(b))

print(sorted(result))
Output:
[3, 4, 5]
Explanation: & finds the intersection of two sets. 93. Find missing number from 1 to N
numbers = [1, 2, 4, 5, 6]

n = 6

expected = n \* (n + 1) // 2
actual = sum(numbers)

print(expected - actual)
Output:
3
Explanation: Subtract the actual sum from the expected sum.
Assumption: Exactly one number is missing from the range 1 to N, with no duplicates. 94. Rotate a list to the right by K positions
numbers = [1, 2, 3, 4, 5]
k = 2

k = k % len(numbers)

result = numbers[-k:] + numbers[:-k]

print(result)
Output:
[4, 5, 1, 2, 3]
Explanation: Split the list and move the last K elements to the beginning. 95. Find the pair whose sum equals the target (Two Sum)
numbers = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(numbers):
complement = target - num

    if complement in seen:
        print(seen[complement], i)
        break

    seen[num] = i

Output:
0 1
Explanation:

- Calculate the required complement.
- Check whether it has already been seen.
- Store previously visited numbers and their indices.
  Time complexity: O(n) average.

96. Merge two sorted lists
    a = [1, 3, 5]
    b = [2, 4, 6]

result = []
i = j = 0

while i < len(a) and j < len(b):
if a[i] < b[j]:
result.append(a[i])
i += 1
else:
result.append(b[j])
j += 1

result.extend(a[i:])
result.extend(b[j:])

print(result)
Output:
[1, 2, 3, 4, 5, 6]
Explanation: Compare the current elements of both lists and append the smaller one.
Time complexity: O(n + m). 97. Find the maximum difference between two elements
numbers = [7, 1, 5, 3, 6, 4]

minimum = numbers[0]
max_diff = 0

for num in numbers[1:]:
max_diff = max(max_diff, num - minimum)
minimum = min(minimum, num)

print(max_diff)
Output:
5
Explanation: Find the maximum difference where the smaller element appears before the larger element. 98. Separate positive and negative numbers
numbers = [-2, 5, -7, 8, 3, -1]

positive = []
negative = []

for num in numbers:
if num >= 0:
positive.append(num)
else:
negative.append(num)

print("Positive:", positive)
print("Negative:", negative)
Output:
Positive: [5, 8, 3]
Negative: [-2, -7, -1] 99. Find the intersection of two lists without using sets
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

result = []

for num in a:
if num in b and num not in result:
result.append(num)

print(result)
Output:
[3, 4, 5]
Explanation: Check whether each element exists in both lists and avoid duplicates.
Time complexity: O(n × m) in the worst case. 100. Find the maximum subarray sum (Kadane’s algorithm)
Very important interview question
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = numbers[0]
max_sum = numbers[0]

for num in numbers[1:]:
current_sum = max(num, current_sum + num)
max_sum = max(max_sum, current_sum)

print(max_sum)
Output:
6
Explanation:
The maximum-sum continuous subarray is:
[4, -1, 2, 1]
Its sum is 6.
The algorithm:

- Keep track of the current subarray sum.
- Decide whether to extend the existing subarray or start a new one.
- Track the maximum sum.
  Time complexity: O(n).
  Important list methods for technical interviews
  Method Purpose
  append() Add one element
  extend() Add multiple elements
  insert() Insert at an index
  remove() Remove a value
  pop() Remove and return an element
  sort() Sort the original list
  sorted() Return a new sorted list
  reverse() Reverse the original list
  index() Find an element’s position
  count() Count occurrences
  Important interview complexity table
  Problem Time complexity
  Find largest O(n)
  Find smallest O(n)
  Second largest O(n)
  Reverse using slicing O(n)
  Remove duplicates using set O(n) average
  Find frequency O(n) average
  Move zeros O(n)
  Two Sum O(n) average
  Merge sorted lists O(n + m)
  Kadane’s algorithm O(n)
  Day 5 – Technical interview assessment
  Test yourself on these commonly asked questions.
  Day 5 – Test your Python knowledge

1. What is the time complexity of finding the largest element in a list?
   O(1)
   O(n)
   O(n²)
   O(log n)
2. Which data structure is useful for efficiently tracking duplicates?
   Set
   Float
   String
   Boolean
3. What is the output of 1,2,3,4,5-2:?
   1,2
   3,4,5
   4,5
   5
4. Which algorithm solves the maximum subarray sum problem efficiently?
   Binary Search
   Kadane’s Algorithm
   Bubble Sort
   DFS
5. What is the average time complexity of Two Sum using a dictionary?
   O(n²)
   O(n log n)
   O(n)
   O(1)
6. What does extend() do?
   Deletes a list
   Adds elements from an iterable
   Sorts a list
   Reverses a list
   Submit answers
   Your 100-day Python challenge progress
   Total programs completed
   100 / 2,000
   Day 5 of 100
   5% completed
   What comes next?
   Day 6 – Python Tuple and Set Interview Programs (101–120)
   Topics include:

- Tuple creation and operations.
- Tuple unpacking.
- Convert list into tuple.
- Find duplicate elements using sets.
- Union and intersection.
- Difference and symmetric difference.
- Remove duplicates using sets.
- Frozen sets.
- Set comprehension.
- Real-world tuple and set interview problems.
  Interview tip: Practise writing each of today’s 20 programs without looking at the solution. Understanding the logic is more important than memorising the code.

Day 6 – Python Tuple and Set Coding Interview Programs (101–120)
Today’s topics: Tuples, Sets, Frozen Sets, Set Operations, Tuple Unpacking and Frequently Asked Python Interview Questions.
Tuples and sets are important Python data structures. Interviewers commonly ask questions about immutability, duplicate removal, membership testing, union, intersection and differences.
Part 1 – Python Tuple Programs (101–110) 101. Create a tuple and access elements
Question: Create a tuple and print its first, last and middle elements.
numbers = (10, 20, 30, 40, 50)

print("First:", numbers[0])
print("Last:", numbers[-1])
print("Middle:", numbers[2])
Output:
First: 10
Last: 50
Middle: 30
Explanation:

- Tuples store multiple values.
- Indexing starts from zero.
- Negative indexing accesses elements from the end.
- Tuples are immutable.
  Time complexity: O(1) for each indexed access.

102. Find the length of a tuple
     numbers = (10, 20, 30, 40, 50)

print(len(numbers))
Output:
5
Explanation: len() returns the number of elements in a tuple.
Time complexity: O(1). 103. Find the maximum and minimum elements
numbers = (10, 50, 20, 5, 40)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
Output:
Maximum: 50
Minimum: 5
Explanation: max() finds the largest value and min() finds the smallest value.
Time complexity: O(n). 104. Convert a list into a tuple
numbers = [10, 20, 30, 40]

result = tuple(numbers)

print(result)
Output:
(10, 20, 30, 40)
Explanation: The tuple() constructor converts an iterable into a tuple.
Time complexity: O(n). 105. Convert a tuple into a list
numbers = (10, 20, 30, 40)

result = list(numbers)

print(result)
Output:
[10, 20, 30, 40]
Explanation: Use list() to convert a tuple into a mutable list.
Time complexity: O(n). 106. Count occurrences of an element in a tuple
numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))
Output:
3
Explanation: count() returns how many times a particular element appears.
Time complexity: O(n). 107. Find the index of an element in a tuple
numbers = (10, 20, 30, 40, 50)

print(numbers.index(30))
Output:
2
Explanation: index() returns the first occurrence’s position.
Time complexity: O(n). 108. Unpack a tuple into variables
person = ("John", 25, "Python Developer")

name, age, job = person

print(name)
print(age)
print(job)
Output:
John
25
Python Developer
Explanation: Tuple unpacking assigns tuple elements to individual variables.
Time complexity: O(n) for unpacking n elements. 109. Swap two variables using tuple unpacking
a = 10
b = 20

a, b = b, a

print("a:", a)
print("b:", b)
Output:
a: 20
b: 10
Explanation: Python supports multiple assignment, allowing variables to be swapped without a temporary variable.
Time complexity: O(1). 110. Sort a tuple
numbers = (50, 10, 40, 20, 30)

result = tuple(sorted(numbers))

print(result)
Output:
(10, 20, 30, 40, 50)
Explanation:

- sorted() returns a sorted list.
- tuple() converts the sorted list back into a tuple.
- The original tuple remains unchanged.
  Time complexity: O(n log n).
  Part 2 – Python Set Programs (111–120)

111. Create a set and remove duplicates
     Frequently asked
     numbers = [10, 20, 10, 30, 20, 40]

result = set(numbers)

print(result)
Output:
{10, 20, 30, 40}
Explanation:

- Sets store unique elements.
- Duplicate elements are automatically removed.
- Sets are unordered collections.
  Time complexity: O(n) average.

112. Find the union of two sets
     a = {1, 2, 3, 4}
     b = {3, 4, 5, 6}

result = a.union(b)

print(result)
Output:
{1, 2, 3, 4, 5, 6}
Explanation: Union combines all unique elements from both sets.
Alternative:
result = a | b
Time complexity: O(n + m) average. 113. Find the intersection of two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.intersection(b)

print(result)
Output:
{3, 4}
Explanation: Intersection returns elements common to both sets.
Alternative:
result = a & b
Time complexity: O(min(n, m)) average under typical hash-set assumptions. 114. Find the difference between two sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.difference(b)

print(result)
Output:
{1, 2}
Explanation: Difference returns elements present in the first set but not in the second.
Alternative:
result = a - b
Time complexity: O(n) average. 115. Find symmetric difference
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

result = a.symmetric_difference(b)

print(result)
Output:
{1, 2, 5, 6}
Explanation: Symmetric difference returns elements that belong to either set, but not both.
Alternative:
result = a ^ b
Time complexity: O(n + m) average. 116. Check whether two sets are disjoint
a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))
Output:
True
Explanation: Two sets are disjoint when they have no common elements.
Time complexity: O(min(n, m)) average. 117. Check whether one set is a subset of another
a = {1, 2}
b = {1, 2, 3, 4, 5}

print(a.issubset(b))
Output:
True
Explanation: A is a subset of B when every element in A exists in B.
Alternative:
print(a <= b)
Time complexity: O(n) average. 118. Check whether one set is a superset of another
a = {1, 2, 3, 4, 5}
b = {1, 2}

print(a.issuperset(b))
Output:
True
Explanation: A is a superset of B when A contains every element of B.
Alternative:
print(a >= b)
Time complexity: O(m) average, where m is the size of B. 119. Find duplicate elements using sets
Common coding interview question
numbers = [1, 2, 3, 2, 4, 5, 3, 6]

seen = set()
duplicates = set()

for num in numbers:
if num in seen:
duplicates.add(num)
else:
seen.add(num)

print(duplicates)
Output:
{2, 3}
Explanation:

- Create an empty set called seen.
- Check whether each element already exists.
- If it exists, add it to duplicates.
- Otherwise, add it to seen.
  Time complexity: O(n) average.

120. Use a frozen set
     numbers = frozenset([10, 20, 30, 40])

print(numbers)

print(20 in numbers)
Output:
frozenset({10, 20, 30, 40})
True
Explanation:

- frozenset() creates an immutable set.
- You cannot add or remove elements.
- Frozen sets can be used as dictionary keys or set elements, provided their elements are hashable.
  Time complexity:
- Creation: O(n) average.
- Membership check: O(1) average.
  Important Python interview concepts

1. Difference between List, Tuple and Set
   Feature List Tuple Set
   Syntax [] () {}
   Ordered Yes Yes No
   Mutable Yes No Yes
   Duplicates Yes Yes No
   Indexing Yes Yes No
   Hashable No Sometimes No
2. Important tuple and set methods
   Tuple methods Set methods
   count() add()
   index() update()
   len() remove()
   max() discard()
   min() union()
   sorted() intersection()
   tuple() difference()
   symmetric_difference()
   issubset()
   issuperset()
3. Important interview differences
   Q1. What is the difference between remove() and discard() in sets?
   a = {1, 2, 3}

a.remove(2) # Removes 2
a.discard(5) # No error if 5 is absent

- remove() raises KeyError if the element doesn’t exist.
- discard() does not raise an error if the element doesn’t exist.
  Q2. Can a tuple contain a list?
  Yes.
  a = (10, 20, [30, 40])

a[2].append(50)

print(a)
Output:
(10, 20, [30, 40, 50])
Explanation: A tuple is immutable, but a mutable object stored inside it can still be modified.
Q3. Can we create an empty set using {}?
No.
a = {}
b = set()

print(type(a))
print(type(b))
Output:
<class 'dict'>
<class 'set'>
Use set() to create an empty set.
Day 6 – Technical interview assessment
Try these questions without looking at the answers.
Day 6 assessment
7 questions

1. Which data structure does not allow duplicate elements?
   List
   Tuple
   Set
   Dictionary
2. Are tuples mutable or immutable?
   Mutable
   Immutable
   Both
   Neither
3. Which operator finds the intersection of two sets?
   |
   &

- ●
  ^

4. What does discard() do when an element is missing?
   Raises KeyError
   Returns an error
   Does nothing
   Deletes the set
5. Which creates an empty set?
   {}

set()
() 6. Which method returns elements present in either set but not both?
union()
intersection()
difference()
symmetric_difference() 7. Can a frozen set be used as a dictionary key?
Yes, if its elements are hashable
No
Only if empty
Only with integers
Submit answers
Your 100-day Python challenge progress
Programs completed
120 / 2,000
Day 6 of 100
6% completed
Coming next – Day 7
Python Dictionary Coding Interview Programs (121–140)
We will cover:

- Create and access dictionaries.
- Find key and value pairs.
- Count character frequency.
- Find duplicate dictionary values.
- Merge two dictionaries.
- Sort dictionary by keys.
- Sort dictionary by values.
- Find the maximum and minimum values.
- Dictionary comprehension.
- Two dictionaries comparison.
- Invert dictionary keys and values.
- Group elements using dictionaries.
- Find common keys.
- Nested dictionaries.
- Real-world dictionary interview problems.
  My recommendation: Spend 30–45 minutes coding today’s 20 programs yourself. Pay special attention to set operations and tuple immutability because interviewers often ask conceptual follow-up questions about them.

Day 7 – 20 Python Dictionary Coding Interview Programs
Day 7 of 100Programs 121–140
Topic: Python Dictionaries (dict)
Dictionaries are one of the most important Python interview topics. They store data as key-value pairs and provide average lookup, insertion, and deletion.

1. Create and print a dictionary
   Program 121
   student = {
   "name": "John",
   "age": 22,
   "course": "Python"
   }

print(student)
Explanation: Creates a dictionary containing three key-value pairs.
Output:
{'name': 'John', 'age': 22, 'course': 'Python'}
Time complexity: for each insertion; overall. 2. Access dictionary values
Program 122
student = {
"name": "John",
"age": 22,
"course": "Python"
}

print(student["name"])
print(student.get("age"))
print(student.get("city", "Not found"))
Explanation:

- student["name"] accesses a value using its key.
- get() safely accesses a key.
- get() can return a default value if the key is missing.
  Output:
  John
  22
  Not found
  Time complexity: average per lookup.

3. Print all dictionary keys and values
   Program 123
   student = {
   "name": "John",
   "age": 22,
   "course": "Python"
   }

for key, value in student.items():
print(key, ":", value)
Explanation: items() returns key-value pairs that can be unpacked in a loop.
Output:
name : John
age : 22
course : Python
Time complexity: . 4. Count character frequency in a string
Program 124
text = "programming"

frequency = {}

for char in text:
frequency[char] = frequency.get(char, 0) + 1

print(frequency)
Explanation: Counts how many times each character appears. get(char, 0) returns zero when the character is not yet present.
Output:
{'p': 1, 'r': 2, 'o': 1, 'g': 2,
'a': 1, 'm': 2, 'i': 1, 'n': 1}
Time complexity: average. 5. Find duplicate values in a dictionary
Program 125
data = {
"a": 10,
"b": 20,
"c": 10,
"d": 30,
"e": 20
}

seen = set()
duplicates = set()

for value in data.values():
if value in seen:
duplicates.add(value)
else:
seen.add(value)

print(duplicates)
Explanation: A set stores values already encountered. If a value appears again, it is added to the duplicates set.
Output:
{10, 20}
Time complexity: average. 6. Merge two dictionaries
Program 126
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}

print(merged)
Explanation: Dictionary unpacking (\*\*) combines both dictionaries. If keys overlap, the value from the second dictionary wins.
Output:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
Time complexity: . 7. Sort dictionary by keys
Program 127
data = {
"banana": 3,
"apple": 5,
"orange": 2
}

sorted_data = dict(sorted(data.items()))

print(sorted_data)
Explanation: sorted() sorts dictionary items by their keys by default.
Output:
{'apple': 5, 'banana': 3, 'orange': 2}
Time complexity: . 8. Sort dictionary by values
Program 128
data = {
"apple": 5,
"banana": 3,
"orange": 2
}

sorted_data = dict(
sorted(data.items(), key=lambda item: item[1])
)

print(sorted_data)
Explanation: The key function selects the value (item[1]) as the sorting criterion.
Output:
{'orange': 2, 'banana': 3, 'apple': 5}
Time complexity: . 9. Find the key with the maximum value
Program 129
marks = {
"John": 85,
"Alice": 95,
"Bob": 75
}

maximum_key = max(marks, key=marks.get)

print(maximum_key)
print(marks[maximum_key])
Explanation: max() finds the key whose associated value is highest.
Output:
Alice
95
Time complexity: . 10. Find the key with the minimum value
Program 130
marks = {
"John": 85,
"Alice": 95,
"Bob": 75
}

minimum_key = min(marks, key=marks.get)

print(minimum_key)
print(marks[minimum_key])
Explanation: min() finds the key associated with the smallest value.
Output:
Bob
75
Time complexity: . 11. Create a dictionary using dictionary comprehension
Program 131
numbers = [1, 2, 3, 4, 5]

squares = {
num: num \*\* 2
for num in numbers
}

print(squares)
Explanation: Dictionary comprehension creates a dictionary in a compact way.
Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Time complexity: . 12. Compare two dictionaries
Program 132
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}

if dict1 == dict2:
print("Dictionaries are equal")
else:
print("Dictionaries are not equal")
Explanation: Dictionary equality checks whether both dictionaries contain the same key-value pairs. Their insertion order does not matter.
Output:
Dictionaries are equal
Time complexity: average. 13. Reverse dictionary keys and values
Program 133
data = {
"a": 1,
"b": 2,
"c": 3
}

reversed_dict = {
value: key
for key, value in data.items()
}

print(reversed_dict)
Explanation: Swaps each key and value. Original values must be hashable. Duplicate values in the original dictionary will overwrite earlier entries.
Output:
{1: 'a', 2: 'b', 3: 'c'}
Time complexity: average. 14. Group words by their first character
Program 134
words = ["apple", "ant", "banana", "ball", "cat"]

grouped = {}

for word in words:
first = word[0]

    if first not in grouped:
        grouped[first] = []

    grouped[first].append(word)

print(grouped)
Explanation: Groups words into lists based on their first character.
Output:
{
'a': ['apple', 'ant'],
'b': ['banana', 'ball'],
'c': ['cat']
}
Time complexity: for a fixed-size alphabet and bounded word lengths; more generally, , where is the total number of characters processed. 15. Find common keys between two dictionaries
Program 135
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

common_keys = dict1.keys() & dict2.keys()

print(common_keys)
Explanation: The & operator finds keys that exist in both dictionaries.
Output:
{'b', 'c'}
Time complexity: average. 16. Count word frequency in a sentence
Program 136
sentence = "python is easy and python is powerful"

frequency = {}

for word in sentence.split():
frequency[word] = frequency.get(word, 0) + 1

print(frequency)
Explanation: Splits the sentence into words and counts each word’s occurrences.
Output:
{
'python': 2,
'is': 2,
'easy': 1,
'and': 1,
'powerful': 1
}
Time complexity: , where is the number of characters in the sentence. 17. Access values from a nested dictionary
Program 137
students = {
"student1": {
"name": "John",
"marks": 85
},
"student2": {
"name": "Alice",
"marks": 95
}
}

print(students["student1"]["name"])
print(students["student2"]["marks"])
Explanation: A dictionary can contain another dictionary as its value. Use consecutive keys to access nested values.
Output:
John
95
Time complexity: average for each lookup. 18. Calculate total marks for each student
Program 138
students = {
"John": [80, 85, 90],
"Alice": [90, 95, 100],
"Bob": [70, 75, 80]
}

totals = {}

for name, marks in students.items():
totals[name] = sum(marks)

print(totals)
Explanation: Iterates through each student’s marks and calculates the total using sum().
Output:
{'John': 255, 'Alice': 285, 'Bob': 225}
Time complexity: , where is the number of students and is the average number of marks per student. 19. Find the second-highest dictionary value
Program 139
data = {
"a": 10,
"b": 50,
"c": 30,
"d": 40
}

unique_values = sorted(set(data.values()))

if len(unique_values) >= 2:
print(unique_values[-2])
else:
print("Second-highest value does not exist")
Explanation: Removes duplicate values, sorts them, and selects the second-largest distinct value.
Output:
40
Time complexity: . 20. Find the first non-repeating character using a dictionary
Program 140
text = "aabbcde"

frequency = {}

for char in text:
frequency[char] = frequency.get(char, 0) + 1

for char in text:
if frequency[char] == 1:
print("First non-repeating character:", char)
break
else:
print("No non-repeating character")
Explanation: First counts each character. Then it scans the original string to find the first character with a frequency of one.
Output:
First non-repeating character: c
Time complexity: average.
Day 7 – Important interview concepts
Dictionary operation Average time complexity
Access by key
Insert key-value pair
Update value
Delete key
Search for key
Iterate through dictionary
Sort dictionary items
Note: These are average-case hash-table complexities. In unusual collision-heavy cases, individual operations can take .
Day 7 – Interview practice checklist
Your practice progress
0/10
Create a dictionary and access its values
Count character frequency
Merge two dictionaries
Sort dictionary by values
Find maximum and minimum values
Reverse dictionary keys and values
Group words using a dictionary
Find common keys
Find the second-highest value
Find the first non-repeating character
Completed: 140 / 2,000 programs
Next: Day 8 – Python Functions and Recursion (Programs 141–160), covering recursion, lambda functions, map(), filter(), reduce(), and common function-based interview problems.

Day 8 – 20 Python Functions and Recursion Coding Interview Programs
Day 8 of 100Programs 141–160
Topics covered: Functions, arguments, return values, lambda, recursion, map(), filter(), reduce(), and common interview problems.
Functions and recursion are frequently tested in Python technical interviews. Practise understanding not only the output but also how arguments and return values work.

1. Create a simple function
   Program 141
   def greet():
   print("Hello, Python!")

greet()
Explanation: A function is a reusable block of code. def defines the function, and greet() calls it.
Output:
Hello, Python!
Time complexity: . 2. Function with parameters
Program 142
def add(a, b):
print("Sum:", a + b)

add(10, 20)
Explanation: Parameters receive values when the function is called. Here, a receives 10 and b receives 20.
Output:
Sum: 30
Time complexity: . 3. Function with a return statement
Program 143
def multiply(a, b):
return a \* b

result = multiply(5, 4)

print(result)
Explanation: return sends a result back to the caller instead of simply printing it.
Output:
20
Time complexity: . 4. Find factorial using a function
Program 144
def factorial(n):
result = 1

    for i in range(1, n + 1):
        result *= i

    return result

print(factorial(5))
Explanation: Multiplies all integers from 1 through n. The factorial of 5 is .
Output:
120
Time complexity: . 5. Find factorial using recursion
Program 145
def factorial(n):
if n == 0 or n == 1:
return 1

    return n * factorial(n - 1)

print(factorial(5))
Explanation: Recursion occurs when a function calls itself. The base case stops the recursive calls.
Output:
120
Time complexity: .
Interview point: Recursive factorial uses call-stack space. 6. Find Fibonacci using recursion
Program 146
def fibonacci(n):
if n <= 1:
return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
print(fibonacci(i), end=" ")
Explanation: Each Fibonacci number is the sum of the previous two numbers.
Output:
0 1 1 2 3 5 8
Time complexity: approximately for this simple recursive implementation.
Interview point: This approach repeats calculations. Memoization or iteration can improve performance to . 7. Find the sum of numbers using
*args
Program 147
def calculate_sum(*args):
return sum(args)

print(calculate_sum(10, 20, 30, 40))
Explanation: \*args allows a function to accept any number of positional arguments.
Output:
100
Time complexity: , where is the number of arguments. 8. Use
**kwargs
in a function
Program 148
def display_details(**kwargs):
for key, value in kwargs.items():
print(key, ":", value)

display_details(
name="John",
age=25,
city="London"
)
Explanation: \*\*kwargs collects keyword arguments into a dictionary.
Output:
name : John
age : 25
city : London
Time complexity: , where is the number of keyword arguments. 9. Find the largest number using a lambda function
Program 149
maximum = lambda a, b: a if a > b else b

print(maximum(25, 40))
Explanation: A lambda is a small anonymous function written in a single expression.
Output:
40
Time complexity: . 10. Square numbers using
map()
Program 150
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x \*\* 2, numbers))

print(squares)
Explanation: map() applies a function to every item in an iterable.
Output:
[1, 4, 9, 16, 25]
Time complexity: . 11. Filter even numbers using
filter()
Program 151
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(
filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)
Explanation: filter() selects elements for which the supplied function returns True.
Output:
[2, 4, 6, 8]
Time complexity: . 12. Calculate the sum using
reduce()
Program 152
from functools import reduce

numbers = [10, 20, 30, 40]

result = reduce(lambda a, b: a + b, numbers)

print(result)
Explanation: reduce() repeatedly combines elements to produce a single result.
Output:
100
Time complexity: . 13. Find the power of a number using recursion
Program 153
def power(base, exponent):
if exponent == 0:
return 1

    return base * power(base, exponent - 1)

print(power(2, 5))
Explanation: Multiplies the base by itself repeatedly until the exponent reaches zero. This implementation assumes a non-negative integer exponent.
Output:
32
Time complexity: , where is the exponent.
Interview improvement: Exponentiation by squaring can reduce this to . 14. Find the sum of digits using recursion
Program 154
def digit_sum(n):
if n == 0:
return 0

    return n % 10 + digit_sum(n // 10)

print(digit_sum(12345))
Explanation: Gets the last digit using % 10, then removes it using integer division.
Output:
15
Time complexity: , where is the number of digits. 15. Check palindrome using a function
Program 155
def is_palindrome(text):
return text == text[::-1]

print(is_palindrome("madam"))
print(is_palindrome("python"))
Explanation: A palindrome reads the same forward and backward. String slicing reverses the string.
Output:
True
False
Time complexity: . 16. Check prime number using a function
Program 156
def is_prime(n):
if n < 2:
return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(17))
print(is_prime(20))
Explanation: Checks whether any number from 2 through the square root of n divides it exactly.
Output:
True
False
Time complexity: . 17. Find the maximum number using
*args
Program 157
def find_max(*args):
if not args:
return None

    return max(args)

print(find_max(10, 50, 20, 80, 30))
Explanation: Accepts multiple positional arguments and returns the largest. The empty-input check prevents an error from max().
Output:
80
Time complexity: . 18. Use a function as an argument
Program 158
def square(x):
return x \* x

def calculate(func, number):
return func(number)

print(calculate(square, 5))
Explanation: Python allows functions to be passed as arguments to other functions. Such functions are often called higher-order functions.
Output:
25
Time complexity: for this square function and input. 19. Create a closure in Python
Program 159
def outer_function(x):
def inner_function(y):
return x + y

    return inner_function

add_ten = outer_function(10)

print(add_ten(5))
print(add_ten(20))
Explanation: A closure is an inner function that remembers variables from its enclosing function even after the outer function has returned.
Output:
15
30
Time complexity: per call. 20. Create a recursive countdown
Program 160
def countdown(n):
if n == 0:
print("Go!")
return

    print(n)
    countdown(n - 1)

countdown(5)
Explanation: The function calls itself with a smaller number until it reaches the base case, zero.
Output:
5
4
3
2
1
Go!
Time complexity: .
Space complexity: because of recursive function calls.
Day 8 – Important Python interview concepts
Concept Purpose
def Defines a function
return Returns a result
*args Accepts multiple positional arguments
\*\*kwargs Accepts multiple keyword arguments
lambda Creates an anonymous function
map() Transforms iterable elements
filter() Selects matching elements
reduce() Combines elements into one result
Recursion Function calls itself
Closure Inner function remembers outer variables
Day 8 – Practice checklist
Practice progress
0/10
Write a function with parameters and return values
Calculate factorial using recursion
Generate Fibonacci numbers
Use *args and \*\*kwargs
Write a lambda function
Use map() to square numbers
Use filter() to select even numbers
Use reduce() to calculate a sum
Check prime and palindrome using functions
Create a closure and recursive countdown
Your 100-day Python challenge
Day 8 completed
160 / 2,000
8% of the 2,000-program challenge completed.
Next: Day 9 – Python Object-Oriented Programming (OOP), Programs 161–180, covering classes, objects, constructors, inheritance, polymorphism, encapsulation, abstraction, and practical interview problems.

Day 9 – 20 Python OOP Coding Interview Programs
Day 9 of 100Programs 161–180
Topic: Object-Oriented Programming (OOP) in Python
OOP is one of the most frequently tested topics in Python technical interviews. You should understand these four pillars:

- Encapsulation – Bundling data and methods together.
- Inheritance – Reusing properties and methods from another class.
- Polymorphism – Using the same interface for different behaviours.
- Abstraction – Hiding implementation details and exposing essential functionality.
  Let’s practise 20 important programs.

1. Create a class and object
   Program 161
   class Student:
   def display(self):
   print("Welcome to Python OOP")

s1 = Student()
s1.display()
Explanation:

- class defines a class.
- Student() creates an object.
- s1.display() calls the method.
  Output:
  Welcome to Python OOP
  Time complexity: .

2.  Create a constructor using
    **init**()
    Program 162
    class Student:
    def **init**(self, name, age):
    self.name = name
    self.age = age

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)

s1 = Student("John", 22)
s1.display()
Explanation: The **init**() method initializes an object’s attributes when the object is created. self refers to the current object.
Output:
Name: John
Age: 22
Time complexity: . 3. Create multiple objects from one class
Program 163
class Employee:
def **init**(self, name, salary):
self.name = name
self.salary = salary

    def display(self):
        print(self.name, self.salary)

e1 = Employee("Alice", 30000)
e2 = Employee("Bob", 40000)

e1.display()
e2.display()
Explanation: A single class can create multiple independent objects with different attribute values.
Output:
Alice 30000
Bob 40000
Time complexity: per object creation and display. 4. Implement instance variables and class variables
Program 164
class Student:
school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("John")
s2 = Student("Alice")

print(s1.name)
print(s2.name)
print(s1.school)
print(s2.school)
Explanation:

- school is a class variable shared through the class.
- name is an instance variable belonging to each object.
  Output:
  John
  Alice
  ABC School
  ABC School
  Time complexity: per attribute access.

5. Implement inheritance
   Program 165
   class Animal:
   def eat(self):
   print("Animal is eating")

class Dog(Animal):
def bark(self):
print("Dog is barking")

d = Dog()
d.eat()
d.bark()
Explanation: Dog inherits the eat() method from Animal. It also has its own bark() method.
Output:
Animal is eating
Dog is barking
Time complexity: per method call. 6. Implement multilevel inheritance
Program 166
class Grandparent:
def show_grandparent(self):
print("Grandparent class")

class Parent(Grandparent):
def show_parent(self):
print("Parent class")

class Child(Parent):
def show_child(self):
print("Child class")

c = Child()

c.show_grandparent()
c.show_parent()
c.show_child()
Explanation: In multilevel inheritance, one class inherits from another class, which itself inherits from a third class.
Output:
Grandparent class
Parent class
Child class
Time complexity: per method call. 7. Implement multiple inheritance
Program 167
class Father:
def father_skill(self):
print("Gardening")

class Mother:
def mother_skill(self):
print("Cooking")

class Child(Father, Mother):
def child_skill(self):
print("Programming")

c = Child()

c.father_skill()
c.mother_skill()
c.child_skill()
Explanation: Multiple inheritance allows a class to inherit from more than one parent class.
Output:
Gardening
Cooking
Programming
Time complexity: per method call. 8. Implement method overriding
Program 168
class Animal:
def sound(self):
print("Animal makes a sound")

class Dog(Animal):
def sound(self):
print("Dog barks")

d = Dog()
d.sound()
Explanation: Method overriding occurs when a child class provides its own implementation of a method inherited from its parent.
Output:
Dog barks
Time complexity: . 9. Implement polymorphism
Program 169
class Dog:
def sound(self):
print("Bark")

class Cat:
def sound(self):
print("Meow")

def make_sound(animal):
animal.sound()

make_sound(Dog())
make_sound(Cat())
Explanation: Both objects provide the same sound() interface but behave differently. This is an example of runtime polymorphism through duck typing.
Output:
Bark
Meow
Time complexity: per call. 10. Implement encapsulation
Program 170
class BankAccount:
def **init**(self, balance):
self.\_\_balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

print(account.get_balance())
Explanation: The double underscore triggers name mangling, making direct access less convenient. Python does not enforce strict private access, but this convention helps protect internal attributes.
Output:
5000
Time complexity: . 11. Implement a getter and setter using properties
Program 171
class Student:
def **init**(self, age):
self.\_age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Invalid age")

s = Student(20)

print(s.age)

s.age = 25
print(s.age)

s.age = -5
Explanation: @property allows attribute-style access to a getter and setter. The setter validates the new value before updating it.
Output:
20
25
Invalid age
Time complexity: per operation. 12. Implement abstraction using an abstract class
Program 172
from abc import ABC, abstractmethod

class Shape(ABC):
@abstractmethod
def area(self):
pass

class Rectangle(Shape):
def **init**(self, length, width):
self.length = length
self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(10, 5)

print("Area:", r.area())
Explanation: An abstract class defines a required interface. A concrete subclass must implement its abstract methods before it can be instantiated.
Output:
Area: 50
Time complexity: for this area calculation. 13. Use the
super()
function
Program 173
class Parent:
def **init**(self):
print("Parent constructor")

class Child(Parent):
def **init**(self):
super().**init**()
print("Child constructor")

c = Child()
Explanation: super() calls the next implementation in the method resolution order (MRO). Here, it invokes the parent constructor.
Output:
Parent constructor
Child constructor
Time complexity: . 14. Implement a static method
Program 174
class Calculator:
@staticmethod
def add(a, b):
return a + b

print(Calculator.add(10, 20))
Explanation: A static method belongs to the class namespace but does not automatically receive self or cls.
Output:
30
Time complexity: . 15. Implement a class method
Program 175
class Employee:
company = "Google"

    @classmethod
    def change_company(cls, name):
        cls.company = name

Employee.change_company("Microsoft")

print(Employee.company)
Explanation: A class method receives the class as its first argument, conventionally called cls. It can access and modify class-level attributes.
Output:
Microsoft
Time complexity: . 16. Overload an operator using
**add**()
Program 176
class Number:
def **init**(self, value):
self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(10)
n2 = Number(20)

result = n1 + n2

print(result.value)
Explanation: Operator overloading allows custom objects to define how operators such as + behave. Python calls **add**() for this operation.
Output:
30
Time complexity: . 17. Implement the
**str**()
method
Program 177
class Student:
def **init**(self, name, age):
self.name = name
self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

s = Student("John", 22)

print(s)
Explanation: **str**() defines the human-readable string representation of an object. It is used by print().
Output:
John is 22 years old
Time complexity: , where is the length of the generated string. 18. Count the number of objects created
Program 178
class Student:
count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("John")
s2 = Student("Alice")
s3 = Student("Bob")

print("Total objects:", Student.count)
Explanation: A class variable keeps track of how many objects have been created.
Output:
Total objects: 3
Time complexity: per object creation. 19. Implement composition
Program 179
class Engine:
def start(self):
print("Engine started")

class Car:
def **init**(self):
self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

car = Car()
car.start_car()
Explanation: Composition means one class contains an object of another class. A Car has an Engine.
Output:
Engine started
Car started
Time complexity: per method call. 20. Create a simple employee management system
Program 180
class Employee:
def **init**(self, emp_id, name, salary):
self.emp_id = emp_id
self.name = name
self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

    def increase_salary(self, percentage):
        self.salary += self.salary * percentage / 100

e1 = Employee(101, "John", 30000)

e1.display()

e1.increase_salary(10)

print("After salary increase:")
e1.display()
Explanation: This practical program combines constructors, instance variables, methods, and object state modification.
Output:
ID: 101
Name: John
Salary: 30000
After salary increase:
ID: 101
Name: John
Salary: 33000.0
Time complexity: per method call.
Day 9 – Important OOP interview questions
Interview question Key concept
What is a class? Blueprint for objects
What is an object? Instance of a class
What is self? Current instance reference
What is init()? Initializer method
What is inheritance? Reusing parent class behaviour
What is polymorphism? Same interface, different behaviour
What is encapsulation? Bundling and controlling access to data
What is abstraction? Exposing essential interfaces
What is method overriding? Redefining an inherited method
What is super()? Accessing the next class in the MRO
Day 9 – Practice checklist
OOP practice progress
0/14
Create a class and multiple objects
Use constructors and instance variables
Implement single and multilevel inheritance
Implement multiple inheritance
Demonstrate method overriding
Implement polymorphism
Use encapsulation with private attributes
Use getters and setters
Create an abstract class
Use super() correctly
Implement static and class methods
Overload the + operator
Use str()
Build a small employee management system
100-day Python interview challenge
Day 9
180 / 2,000
9% completed – 1,820 programs remaining.
Next: Day 10 – Python Exception Handling and File Handling (Programs 181–200)
We’ll cover try, except, finally, custom exceptions, file reading, writing, appending, CSV handling, and practical file-processing interview questions.

Day 10 – 20 Python Exception Handling and File Handling Coding Interview Programs
Day 10 of 100Programs 181–200
Topics covered:

- Exception handling: try, except, else, finally, raise
- Built-in and custom exceptions
- File handling: read, write, append, close
- Working with text files, CSV and JSON
- File and directory operations
  These are important topics for Python developer interviews because they test how you handle errors and work with real-world data.
  Note: File examples below create or modify files in the current working directory. Their sample outputs show the expected results.
  Part 1 – Exception Handling Programs

1.  Handle division by zero
    Program 181
    try:
    a = 10
    b = 0

        result = a / b
        print(result)

except ZeroDivisionError:
print("Cannot divide by zero")
Explanation:

- try contains code that may cause an exception.
- except handles the specified exception.
- Dividing a number by zero raises ZeroDivisionError.
  Output:
  Cannot divide by zero
  Time complexity: .

2.  Handle multiple exceptions
    Program 182
    try:
    numbers = [10, 20, 30]

        index = int(input("Enter index: "))
        print(numbers[index])

except ValueError:
print("Please enter a valid integer")

except IndexError:
print("Index is out of range")
Explanation:
Different exception types can be handled using separate except blocks.
Sample output (input: 5):
Enter index: 5
Index is out of range
Time complexity: for list indexing. 3. Use the
else
block
Program 183
try:
a = 10
b = 2

    result = a / b

except ZeroDivisionError:
print("Division error")

else:
print("Result:", result)
Explanation:
The else block executes only when no exception occurs in the try block.
Output:
Result: 5.0
Time complexity: . 4. Use the
finally
block
Program 184
try:
print("Inside try block")

    result = 10 / 2
    print(result)

except ZeroDivisionError:
print("Division error")

finally:
print("Finally block executed")
Explanation:
The finally block normally executes whether an exception occurs or not. It is commonly used for cleanup operations.
Output:
Inside try block
5.0
Finally block executed
Time complexity: . 5. Handle a missing dictionary key
Program 185
student = {
"name": "John",
"age": 22
}

try:
print(student["city"])

except KeyError:
print("Key does not exist")
Explanation:
Accessing a missing dictionary key using square brackets raises KeyError.
Output:
Key does not exist
Time complexity: average. 6. Handle a missing file
Program 186
try:
file = open("unknown.txt", "r")
content = file.read()
print(content)

except FileNotFoundError:
print("File not found")
Explanation:
FileNotFoundError occurs when Python cannot find the requested file.
Output (if the file does not exist):
File not found
Time complexity: Depends on the file system and file size. Opening a file is generally treated as for algorithm analysis; reading its contents is . 7. Raise a custom exception using
raise
Program 187
age = 15

try:
if age < 18:
raise ValueError("Age must be 18 or above")

    print("Eligible")

except ValueError as e:
print("Error:", e)
Explanation:
The raise keyword manually triggers an exception when a condition is not satisfied.
Output:
Error: Age must be 18 or above
Time complexity: . 8. Create a custom exception class
Program 188
class InsufficientBalanceError(Exception):
pass

balance = 1000
withdraw = 1500

try:
if withdraw > balance:
raise InsufficientBalanceError(
"Insufficient account balance"
)

    balance -= withdraw
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
print(e)
Explanation:
A custom exception is created by inheriting from Python’s Exception class.
This is useful for application-specific errors such as insufficient balance, invalid age, or unavailable products.
Output:
Insufficient account balance
Time complexity: . 9. Catch multiple exception types in one block
Program 189
try:
a = int("10")
b = int("0")

    print(a / b)

except (ValueError, ZeroDivisionError) as e:
print("Error:", type(e).**name**)
Explanation:
You can handle multiple exception types using a tuple inside one except block.
Output:
Error: ZeroDivisionError
Time complexity: . 10. Use exception handling with a function
Program 190
def divide(a, b):
try:
return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))
Explanation:
Exception handling can be placed inside a function so that errors are handled locally and the caller receives a meaningful result.
Output:
5.0
Cannot divide by zero
Time complexity: .
Part 2 – File Handling Programs 11. Create and write to a file
Program 191
with open("sample.txt", "w") as file:
file.write("Hello Python\n")
file.write("Welcome to file handling")

print("File written successfully")
Explanation:

- "w" opens a file in write mode.
- It creates the file if it does not exist.
- If the file already exists, its previous contents are overwritten.
- with automatically closes the file when the block finishes.
  Output:
  File written successfully
  File content:
  Hello Python
  Welcome to file handling
  Time complexity: , where is the number of characters written.

12. Read the entire contents of a file
    Program 192
    with open("sample.txt", "r") as file:
    content = file.read()

print(content)
Explanation:
The "r" mode opens a file for reading. read() returns the entire file contents as a string.
Output:
Hello Python
Welcome to file handling
Time complexity: , where is the file size. 13. Read a file line by line
Program 193
with open("sample.txt", "r") as file:
for line in file:
print(line.strip())
Explanation:
Iterating over a file reads one line at a time. strip() removes surrounding whitespace, including the newline character.
Output:
Hello Python
Welcome to file handling
Time complexity: , where is the total number of characters.
Interview point: Reading line by line is generally more memory-efficient than loading a very large file all at once. 14. Append data to an existing file
Program 194
with open("sample.txt", "a") as file:
file.write("\nLearning Python")

print("Data appended successfully")
Explanation:
The "a" mode adds new content at the end of a file without deleting existing content.
Output:
Data appended successfully
Updated file content:
Hello Python
Welcome to file handling
Learning Python
Time complexity: , where is the amount of data appended. 15. Count the number of lines in a file
Program 195
with open("sample.txt", "r") as file:
lines = file.readlines()

print("Total lines:", len(lines))
Explanation:
readlines() returns a list containing each line. len() counts the number of lines.
Output:
Total lines: 3
Time complexity: , where is the file size.
Space complexity: , because all lines are loaded into memory. 16. Count words in a file
Program 196
with open("sample.txt", "r") as file:
content = file.read()

words = content.split()

print("Total words:", len(words))
Explanation:
split() separates the contents into whitespace-delimited words, and len() counts them.
Output:
Total words: 7
Time complexity: .
Space complexity: for the resulting word list. 17. Count characters in a file
Program 197
with open("sample.txt", "r") as file:
content = file.read()

print("Total characters:", len(content))
Explanation:
read() loads the file into a string. len() counts the number of Python string characters, not necessarily the number of encoded bytes.
Output (using the three-line sample file above):
Total characters: 64
Time complexity: . 18. Copy contents from one file to another
Program 198
with open("sample.txt", "r") as source:
content = source.read()

with open("copy.txt", "w") as destination:
destination.write(content)

print("File copied successfully")
Explanation:
Reads the contents of one file and writes the same contents into another file.
Output:
File copied successfully
Time complexity: .
Interview improvement: For very large files, copy in chunks instead of reading the entire file into memory. 19. Write and read JSON data
Program 199
import json

student = {
"name": "John",
"age": 22,
"course": "Python"
}

# Write JSON

with open("student.json", "w") as file:
json.dump(student, file, indent=4)

# Read JSON

with open("student.json", "r") as file:
data = json.load(file)

print(data)
print(data["name"])
Explanation:

- json.dump() writes Python data to a JSON file.
- json.load() reads JSON data and converts it into Python objects.
  Output:
  {'name': 'John', 'age': 22, 'course': 'Python'}
  John
  Time complexity: for serialization or deserialization, where is the size of the data.

20. Read and write CSV files
    Program 200
    import csv

# Write CSV file

with open("students.csv", "w", newline="") as file:
writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["John", 22, "Python"])
    writer.writerow(["Alice", 24, "Java"])

# Read CSV file

with open("students.csv", "r") as file:
reader = csv.reader(file)

    for row in reader:
        print(row)

Explanation:

- csv.writer() writes rows into a CSV file.
- writerow() writes one row.
- csv.reader() reads rows from a CSV file.
- newline="" helps avoid extra blank lines when writing CSV files on some platforms.
  Output:
  ['Name', 'Age', 'Course']
  ['John', '22', 'Python']
  ['Alice', '24', 'Java']
  Time complexity: , where is the total amount of CSV data processed.
  Day 10 – Important interview concepts
  Concept Purpose
  try Runs code that may raise an exception
  except Handles an exception
  else Runs if no exception occurred
  finally Runs cleanup code
  raise Manually raises an exception
  Custom exception Defines application-specific errors
  open() Opens a file
  read() Reads file contents
  write() Writes data to a file
  append mode Adds data to the end
  with Automatically manages file closing
  json Reads and writes JSON data
  csv Reads and writes CSV data
  Common file modes to remember
  Mode Meaning
  “r” Read
  “w” Write; overwrites existing content
  “a” Append
  “x” Create; raises an error if the file exists
  “r+” Read and write
  “rb” Read binary
  “wb” Write binary
