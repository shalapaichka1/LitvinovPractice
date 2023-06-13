def center(strng, width, fill=' '):
    a = strng.count('') - 1
    if a == width:
        return strng
    if fill == ' ' and width % 2 == 0:
        return f'{fill * (1+(width - a) // 2)}{strng}{fill * ((width - a) // 2)}'
    elif fill == ' ' and width % 2 != 0:
        return f'{fill * ((width - a) // 2)}{strng}{fill * ((width - a) // 2)}'
    elif (width - a) % 2 == 0:
        return f'{fill * ((width - a) // 2)}{strng}{fill * ((width - a) // 2)}'
    else:
        return f'{fill * (1 + (width - a) // 2)}{strng}{fill * ((width - a) // 2)}'