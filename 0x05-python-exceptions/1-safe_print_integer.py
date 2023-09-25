def safe_print_integer(value):
    try:
        if value is int:
            return True
        else:
            return False
    except ValueError:
        value = value
