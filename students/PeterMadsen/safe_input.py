def safe_input(prompt):
    try:
        return raw_input(prompt)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

# TEST CODE
if __name__ == '__main__':
    print(safe_input("Test Prompt. Please Enter Something: "))
