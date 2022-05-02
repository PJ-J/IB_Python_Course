# Lab 1

def extract_from_list(elements):
    """
    Implement a function to extract certain objects from this list. Test list is [[3,2,6], [4,9,3], [9,6,3]]

    What you will do: extract the 3 from the first list of numbers, the 3 from the second list of numbers, and the 6 from the last list of numbers.
    Yes this is a list of lists
    """

    return [elements[0][1], elements[1][2], elements[2][1]]

print(extract_from_list([[3,2,6], [4,9,3], [9,6,3]]))

def count_e_in_string(string):
    """
    Write a function to go through a string and count the number of Es in the string. You must use iteration in this and also
    need to handle upper and lowercase letters

    Params: string(str), string to count the number of E's
    Returns: int, the number of E's in the string
    """
    return string.lower().count("e")

print(count_e_in_string("Elementary"))

def length_of_string(string):
    """
    Write a function to count the number of characters in  a string. You must use iteration to do this

    Params: string (str), string to count the length
    Returns: int, the length of the string
    """
    return len(string)

print(length_of_string("hotdog"))

def reverse_string(string):
    """
    Write a function to reverse a string. You must use iteration to do this. Hint: think about how objects enter a string and leave a string

    Params: string (str), string to reverse
    Returns: string, the reversed string
    """
    return string[::-1]

print(reverse_string("rocking"))

def concact_elements_in_list(elements):
    """
    Write a function to concact the elements in a list together. You can assume all the elements are of type string. Please be sure to indlude white space between each element.
    I recommend solving this before the next function so you understand how lists work in looping. You must use iteration for this

    Params: elements (list), list of strings
    Returns: string, the newly built string
    """
    return " ".join(elements)

print(concact_elements_in_list(["hello", "you", "are", "hungry"]))

def sum_characters_in_list(elements):
    """
    Write a functuon to sum all the elements in a list. You can assume all the elements are of type int.

    Params: elements (list), list of integers
    Returns: int, the sum of all the integers
    """
    return sum(elements)

print(sum_characters_in_list([3,4,5,6,7]))