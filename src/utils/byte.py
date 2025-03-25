def decode(data: bytes) -> list[str]:
    # Decode the byte data to a string using UTF-8 and split it by underscores
    return data.decode('utf-8').split('_')


def encode(data: str) -> bytes:
    # Ensure the input data is of type string
    assert (type(data) is str)

    length = len(data)

    # If the string is shorter than 10 characters, pad it with hyphens
    if length < 10:
        data += '-' * (10 - length)

    # Convert the string to bytes using UTF-8 encoding
    return bytes(data, 'utf-8')