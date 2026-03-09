from typing import List

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

def main():
    user_list: List[str] = input_list()
    print(user_list)

if __name__ == '__main__':
    main()