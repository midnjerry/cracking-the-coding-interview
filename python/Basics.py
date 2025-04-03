def displayDataTypes():
    displayType("Hello World")
    displayType(20)
    displayType(20.5)
    displayType(1+1j) #Follows format of a + bj where a is real and j represents the imaginary unit
    displayType(["apple", "banana", "cherry"])
    displayType(("apple", "banana", "cherry"))
    displayType(range(6))
    displayType({"name" : "John", "age" : 36})
    displayType({"apple", "banana", "cherry"})
    # A frozen set is like a set, but can't be modified
    displayType(frozenset({"apple", "banana", "cherry"}))
    displayType(True)
    displayType(b"Hello")
    displayType(bytearray(5))
    displayType(memoryview(bytes(5)))
    # Similar to javascript's undefined
    # Is used for variables and functions that do not have a specific value to return
    # To check for None, use `is` and `is not`
    x = None
    if (x is None):
        x = 10
    if (x is not None):
        x = None

    displayType(None)

    
def displayType(x):
    print(f'x = {x} and is of type: {type(x)}')


if __name__ == '__main__':
    displayDataTypes()


# Notes
# Python built-in data types:
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type: dict
# Set Types: set, frozenset
# Boolean Type: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType
# You can use `type(arg)` to get data type of an object.