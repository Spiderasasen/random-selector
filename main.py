from typing import List
import random

# reads the input and returns a list
def input_list() -> List[str]:
    user_list: List[str] = []

    while True:
        user_input: str = input("Type Stop to finish your input.\nPlease enter a list of words: \n")
        user_input: str = user_input.strip().lower()
        if user_input != "stop":
            user_list.append(user_input)
        else:
            break

    return user_list

#selectes a random one
def selctor(user_inputs: List[str]) -> str:
    index: int = random.randint(0, len(user_inputs) - 1)
    return user_inputs[index]

def main():
    user_list: List[str] = input_list()
    print(user_list)
    print(selctor(user_list))

if __name__ == '__main__':
    main()