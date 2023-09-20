COL_LENGTH = 4
ROW_LENGTH = 4


def validate_conditions(pa, ca):
    if pa is None or ca is None:
        return False
    if not isinstance(pa, tuple) or not isinstance(ca, tuple):
        print("pattern or cipher are not tuples.")
        return False
    if len(pa) is not COL_LENGTH or len(ca) is not COL_LENGTH:
        print("Pattern or cipher tuple does not contain 4 elements.")
        return False

    if not all(len(row) == COL_LENGTH for row in ca):
        print("One of the values in cipher tuple does not match column length specifications (4)")
        return False
    if not all(len(row) == COL_LENGTH for row in pa):
        print("One of the values in pattern tuple does not match column length specifications (4)")
        return False
    if not all(all(ch == "X" or ch == "." for ch in row) for row in pa):
        print("All pattern characters must be either X or .")
        return False
    return True


def rotate_matrix(matrix):
    newMatrix = []
    for row, v in enumerate(matrix):
        newString = ""
        for col in range(COL_LENGTH - 1, -1, -1):
            newString += matrix[col][row]
        newMatrix.append(newString)
    return tuple(newMatrix)


def get_indexes(iterable, search):
    indexes = []
    for i, v in enumerate(iterable):
        if v == search:
            indexes.append(i)
    return indexes


def deciper_pattern(pattern, cipher):
    indexes = get_indexes(pattern, 'X')

    decipher = ""
    for index in indexes:
        decipher += cipher[index]
    return decipher


def recall_password(pattern, cipher):
    if not validate_conditions(pattern, cipher):
        return None
    password = ""
    for row in range(ROW_LENGTH):
        for col in range(COL_LENGTH):
            password += deciper_pattern(pattern[col], cipher[col])
        pattern = rotate_matrix(pattern)
    return password


cipher = (
    'BLAI',
    'UMPS',
    'SŠIA',
    'IBUN'
)
print(recall_password((
    '.X.X',
    'X...',
    '....',
    '....'),
    cipher))

