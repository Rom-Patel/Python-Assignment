from assignment_9_1 import File_Operations, MyCustomException

op = File_Operations()

# File operations
try:
    content = op.read_file("output.txt")
    print(content)
except FileNotFoundError as e:
    print(e)

try:
    op.write_file("output.txt", "Hello World!")
except Exception as e:
    print(e)

try:
    op.write_file("output.txt","Python\n")
except Exception as e:
    print(e)


# User-defined exception
try:
    raise MyCustomException("This is a custom exception.")
except MyCustomException as e:
    print(e)
