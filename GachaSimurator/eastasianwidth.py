import unicodedata


def width2(text: str):
    length = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            length += 2
        else:
            length += 1
    return length


def ljust2(text: str, width: int, fillchar: str = ' '):
    length = width2(text)

    return ((text + fillchar * (width - length))
            if width - length > 0 else (text))


# print(ljust2('ああああ', 7) + '_')