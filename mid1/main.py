# Please add your copyright line(s) now.
# Copyright 2022 Shenyou Fan syffan@bu.edu
# Copyright 2022 Yilei Feng fengyl@bu.edu


def ship_size(location):
    location = str(location)
    loc1 = location[0]
    loc2 = location[1]
    loc3 = location[2]
    loc4 = location[3]
    length = 0

    if ord(loc1) < ord('A') or ord(loc1) > ord('J'):
        return False
    if ord(loc3) < ord('A') or ord(loc3) > ord('J'):
        return False
    if ord(loc2) < ord('0') or ord(loc2) > ord('9'):
        return False
    if ord(loc4) < ord('0') or ord(loc4) > ord('9'):
        return False
    # 同一行
    if loc2 == loc4:
        if ord(loc3) > ord(loc1):

            length = ord(loc3) - ord(loc1) + 1
            return length
        else:
            length = ord(loc1) - ord(loc3) + 1
            return length

    if loc1 == loc3:
        if ord(loc4) > ord(loc2):
            length = ord(loc4) - ord(loc2) + 1
            return length
        else:
            length = ord(loc2) - ord(loc4) + 1
            return length
    if loc2 != loc4 and loc1 != loc3:
        return False
    # 同一列



def test_ships(ships):
    if len(ships) == 5:

        ship1 = ships[0]
        ship2 = ships[1]
        ship3 = ships[2]
        ship4 = ships[3]
        ship5 = ships[4]

    else:
        return False

    ############################################## 对于ship1
    loc1 = ship1[0]
    loc2 = ship1[1]
    loc3 = ship1[2]
    loc4 = ship1[3]

    if loc1 == loc3:
        n = ord(loc4) - ord(loc2) + 1
        ship1_spread = []
        for i in range(n):
            loc = loc1 + chr(i + ord(loc2))
            ship1_spread.append(loc)
    #         print(ship1_spread)

    if loc2 == loc4:
        n = ord(loc3) - ord(loc1) + 1
        ship1_spread = []
        for i in range(n):
            loc = chr(i + ord(loc1)) + loc2
            ship1_spread.append(loc)
    #         print(ship1_spread)

    ################################################ 对于ship2
    loc1 = ship2[0]
    loc2 = ship2[1]
    loc3 = ship2[2]
    loc4 = ship2[3]

    if loc1 == loc3:
        n = ord(loc4) - ord(loc2) + 1
        ship2_spread = []
        for i in range(n):
            loc = loc1 + chr(i + ord(loc2))
            ship2_spread.append(loc)
    #         print(ship1_spread)

    if loc2 == loc4:
        n = ord(loc3) - ord(loc1) + 1
        ship2_spread = []
        for i in range(n):
            loc = chr(i + ord(loc1)) + loc2
            ship2_spread.append(loc)

    ############################################ 对于ship3
    loc1 = ship3[0]
    loc2 = ship3[1]
    loc3 = ship3[2]
    loc4 = ship3[3]

    if loc1 == loc3:
        n = ord(loc4) - ord(loc2) + 1
        ship3_spread = []
        for i in range(n):
            loc = loc1 + chr(i + ord(loc2))
            ship3_spread.append(loc)
    #         print(ship1_spread)

    if loc2 == loc4:
        n = ord(loc3) - ord(loc1) + 1
        ship3_spread = []
        for i in range(n):
            loc = chr(i + ord(loc1)) + loc2
            ship3_spread.append(loc)

    ############################################ 对于ship4
    loc1 = ship4[0]
    loc2 = ship4[1]
    loc3 = ship4[2]
    loc4 = ship4[3]

    if loc1 == loc3:
        n = ord(loc4) - ord(loc2) + 1
        ship4_spread = []
        for i in range(n):
            loc = loc1 + chr(i + ord(loc2))
            ship4_spread.append(loc)
    #         print(ship1_spread)

    if loc2 == loc4:
        n = ord(loc3) - ord(loc1) + 1
        ship4_spread = []
        for i in range(n):
            loc = chr(i + ord(loc1)) + loc2
            ship4_spread.append(loc)

    ############################################## 对于ship5
    loc1 = ship5[0]
    loc2 = ship5[1]
    loc3 = ship5[2]
    loc4 = ship5[3]

    if loc1 == loc3:
        n = ord(loc4) - ord(loc2) + 1
        ship5_spread = []
        for i in range(n):
            loc = loc1 + chr(i + ord(loc2))
            ship5_spread.append(loc)
    #         print(ship1_spread)

    if loc2 == loc4:
        n = ord(loc3) - ord(loc1) + 1
        ship5_spread = []
        for i in range(n):
            loc = chr(i + ord(loc1)) + loc2
            ship5_spread.append(loc)

    ships_spread = []
    ships_spread.append(ship1_spread)
    ships_spread.append(ship2_spread)
    ships_spread.append(ship3_spread)
    ships_spread.append(ship4_spread)
    ships_spread.append(ship5_spread)
    #     print(ships_spread)

    number = 0
    #     print(number)
    ##### ship1 vs others
    for i in range(4):
        list1 = ships_spread[0]
        list2 = ships_spread[i + 1]
        num = 0
        for item in list1:
            if item in list2:
                return False
            else:
                num += 1
        #         print(i)
        if num == len(list1):
            number += 1

    ##### ship2 vs others
    #     print(number)
    for i in range(3):
        list1 = ships_spread[1]
        list2 = ships_spread[i + 2]
        num = 0

        for item in list1:
            if item in list2:
                return False
            else:
                num += 1
        if num == len(list1):
            number += 1

            ######## ship3 vs others
    #     print(number)
    for i in range(2):
        list1 = ships_spread[2]
        list2 = ships_spread[i + 3]
        num = 0

        for item in list1:
            if item in list2:
                return False
            else:
                num += 1

        if num == len(list1):
            number += 1
    ########## ship4 vs ship5
    #     print(number)
    list1 = ships_spread[3]
    list2 = ships_spread[4]
    num = 0
    for item in list1:
        if item in list2:
            return False
        else:
            num += 1

        if num == len(list1):
            number += 1
    #             print(number)

    #     print(number)

    ships_len = [ship_size(ship1), ship_size(ship2), ship_size(ship3), ship_size(ship4), ship_size(ship5)]
    #     ships_len.sort()
    #     print(ships_len)
    vs_list = [2, 3, 3, 4, 5]
    if ships_len == vs_list:

        if number == 10:
            return True
        else:
            return False
    else:
        return False




good_ships = ['A0A6', "A0J0", "J0A0", "J8J9", "J9J8", "H6H6"]

bad_ships = ["A0J9", "a0a1", "K0K2", "6G7G"]

good_placements = [
    ["A0A1", "B0B2", "C0C2", "D0D3", "E0E4"],
    ["J0J1", "B0B2", "C0C2", "D0D3", "F4B4"],
    ['B1B3', "B4B5", "B6B9", "C2C4", "C5C9"]
]

bad_placements = [
    ["A0A1", "B0B2", "C0C2", "D0D3"],
    ["A0A1", "B0B1", "C8C9", "J8J9", "E5E6"],
    ["B0B1", "B0B2", "C0C2", "D0D3", "E0E4"],
    ["B0B1", "B0B2", "C0C2", "B2E2", "H0H4"],
]


def main():
    try:
        print("testing")

        print("\ngood ships")
        for s in good_ships:
            print(s, ship_size(s))

        print("\nbad ships")
        for s in bad_ships:
            print(s, ship_size(s))

        print("\ngood placements")
        for p in good_placements:
            print(p, test_ships(p))

        print('\nbad placements')
        for p in bad_placements:
            print(p, test_ships(p))
    except Exception as e:
        print("something went wrong:", e)


if __name__ == '__main__':
    main()
