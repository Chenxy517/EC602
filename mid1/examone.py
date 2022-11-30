# Copyright 2022 XingyuChen chxy517@bu.edu
# Copyright 2022 ZhenghaoSun szh1007@bu.edu

def ship_size(s):
    # Check length of string
    if len(s) != 4:
        return False

    # Check character validity
    if ord(s[0]) < ord('A') or ord(s[0]) > ord('J'):
        return False
    if ord(s[2]) < ord('A') or ord(s[2]) > ord('J'):
        return False
    if ord(s[1]) < ord('0') or ord(s[1]) > ord('9'):
        return False
    if ord(s[3]) < ord('0') or ord(s[3]) > ord('9'):
        return False

    # Check location validity
    if ((s[0] != s[2]) and (s[1] != s[3])):
        return False
    elif s[0] == s[2]:
        res = abs(ord(s[3]) - ord(s[1])) + 1
        return res
    elif (s[1] == s[3]):
        res = abs(ord(s[2]) - ord(s[0]))+ 1
        return res

def test_ships(ships):
    # Check number of ships
    if (len(ships) != 5):
        return False
    
    # Set valid list of length
    target_len = [2, 3, 3, 4, 5]
    length = []
    #Check validity of length
    for s in ships:
        size = ship_size(s)
        # Check string validity
        if (size):
            length.append(size)
        else:
            return False
    length.sort()
    if (target_len != length):
        return False

    # Check validity of location
    placed = []
    for s in ships:
        # str_to_int returns a list of index of evry ships
        index = str_to_int(s)
        for coord in index:
            if coord in placed:
                return False
            else:
                placed.append(coord)
    return True
    

# Convert string of ships to index of location
def str_to_int(s):
    output = []
    # Convert string to coordination
    col1 = ord(s[0]) - ord('A')
    row1 = ord(s[1]) - ord('0')
    col2 = ord(s[2]) - ord('A')
    row2 = ord(s[3]) - ord('0')
    for i in range(col1, col2 + 1):
        for j in range(row1, row2 + 1):
            int = j * 10 + i
            output.append(int)
    return output
