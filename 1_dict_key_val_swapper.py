def swap_key_value(dictionary: dict):
    return {v: k for k, v in dictionary.items()}


if __name__ == "__main__":
    try:
        inp = dict()
        # inp = Provide your dict
        result = swap_key_value(inp)
        print(result)
    except Exception as e:
        print(e)
