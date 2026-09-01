def function_1():
    try:
        some_logic_with_value_errors()
    except ValueError as ex:
        print(f"An error ocurred in function_1")


def function_2():
    try:
        some_logic_with_index_errors()
    except IndexError as ex:
        print(f"An error ocurred in function_2")


def main():
    try:
        function_1()
        function_2()
    except Exception as ex:
        print(f"An unexpected error ocurred: {ex}")


if __name__ == "__main__":
    main()
