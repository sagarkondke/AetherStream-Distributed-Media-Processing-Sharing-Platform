import sys

if sys.prefix != sys.base_prefix:
    print("Virtual environment is activated")
    print("Environment path:", sys.prefix)
else:
    print("No virtual environment is active")