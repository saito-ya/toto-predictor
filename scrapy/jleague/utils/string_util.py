def strip(element, target_character):
    if element:
        return element.replace(target_character, '')
    return element

def strip_comma(element):
    return strip(element, ',')

def strip_percent(element):
    return strip(element, '%')
