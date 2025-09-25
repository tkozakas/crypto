COL_LENGTH = 4
ROW_LENGTH = 4

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
    password = ""
    for row in range(ROW_LENGTH):
        for col in range(COL_LENGTH):
            password += deciper_pattern(pattern[col], cipher[col])
        pattern = rotate_matrix(pattern)
    return password

#GENT 
#ORTE 
#HRHE 
#EOTA

#HRLD
#ETRT
#OHSA
#HESN

#EKTO
#DHAR
#RDET
#DHTA

#[0, 6, 8]
correct_pattern = (
    'X...',
    '..X.',
    'X...',
    '....'
)

cipher1 = ('GENT', 'ORTE', 'HRHE', 'EOTA')
cipher2 = ('HRLD', 'ETRT', 'OHSA', 'HESN')
cipher3 = ('EKTO', 'DHAR', 'RDET', 'DHTA')

print("--- Decrypted Messages ---")
print(recall_password(correct_pattern, cipher1))
print(recall_password(correct_pattern, cipher2))
print(recall_password(correct_pattern, cipher3))

