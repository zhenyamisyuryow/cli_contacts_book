


def hello():
    return "Hello! How can I help you?"

def bye():
    return "Good bye!"

func_maps = {
    "hello": hello,
    "add": "add",
    "change": "",
    "get": "",
}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, TypeError, IndexError) as m:
            return f"Error: {m}"
    return wrapper


def handle_input(input:str):
    if input:
        parts = input.lower().split()
        command = parts[0]
        if command in func_maps:
            return parts
    else:
        return Exception


def main():
    while True:
        user_input = handle_input(input(">>> "))
        command = user_input[0]
        if command in ["exit", "close", "bye"]:
            print("Good bye!")
            break
        print(func_maps[command]())

if __name__ == "__main__":
    main()