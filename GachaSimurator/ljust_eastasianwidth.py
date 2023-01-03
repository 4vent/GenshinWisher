import unicodedata


def ljust2(text: str, width: int, fillchar: str = ' '):
    length = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            length += 2
        else:
            length += 1

    return ((text + fillchar * (width - length))
            if width - length > 0 else (text))


# print(ljust2('ああああ', 7) + '_')