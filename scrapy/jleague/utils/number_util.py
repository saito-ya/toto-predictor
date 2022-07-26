def convert_int(element):
    try:
        return int(element)
    except ValueError:
        return 0

def convert_float(element):
    try:
        return float(element)
    except ValueError:
        return 0
