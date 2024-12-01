from util import validate_ages

try:
    validate_ages([24, -5, "ninety", 30, None])
except ExceptionGroup as e:
    print(e)
    print(e.exceptions)
