from collections import deque


def is_palindrome(input_str):
    clean_str = input_str.lower().replace(" ", "")
    char_queue = deque(clean_str)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True



def show(input_string):
    result = is_palindrome(input_string)
    if result:
        print(f'String "{input_string}" - is palindrome.')
    else:
        print(f'String "{input_string}" - is not palindrome.')


if __name__ == "__main__":
    show("littil")
    show("little")
    show("littil ")
    show("littil 1")