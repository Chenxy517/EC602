# Copyright 2022 XingyuChen chxy517@bu.edu
# Copyright 2022 Yimin Xu yxu168@bu.edu
# Copyright 2022 yilei feng fengyl@bu.edu

class Polynomial():
    def __init__(self, s = []):
        length = len(s)
        self.dict = {}
        for i in  range(0, length):
            if s[i] != 0:
                self.dict[length - i - 1] = s[i]

    def __add__(self, other):
        "Return self + other"
        output = Polynomial()
        output.dict = self.dict.copy()
        for key in other.dict.keys():
            if key in output.dict.keys():
                output.dict[key] += other.dict[key]
            else:
                output.dict[key] = other.dict[key]
            if output.dict[key] == 0:
                output.dict.pop(key)
        return output

    def __sub__(self, other):
        "Return self - other"
        output = Polynomial()
        output.dict = self.dict.copy()
        for key in other.dict.keys():
            if key in output.dict.keys():
                output.dict[key] -= other.dict[key]
            else:
                output.dict[key] = -other.dict[key]
            if output.dict[key] == 0:
                output.dict.pop(key)
        return output

    def __mul__(self, other):
        "Return self * other"
        output = Polynomial()
        for key_1 in self.dict.keys():
            for key_2 in other.dict.keys():
                key = key_1 + key_2
                if key in output.dict.keys():
                    output.dict[key] += self.dict[key_1] * other.dict[key_2]
                else:
                    output.dict[key] = self.dict[key_1] * other.dict[key_2]
                if output.dict[key] == 0:
                    output.dict.pop(key)
        return output

    def __eq__(self, other):
        "Return if self equals to other"
        if len(self.dict) != len(other.dict):
            return False
        else:
            for key in self.dict.keys():
                if key not in other.dict.keys():
                    return False
                elif self.dict[key] != other.dict[key]:
                    return False
                else:
                    return True

    def __getitem__(self, index):
        "Get coefficient by key"
        if index not in self.dict.keys():
            return 0
        else:
            return self.dict[index]

    def __setitem__(self, key, val):
        "Set coefficient by key"
        if val == 0:
            self.dict.pop(key)
        else:
            self.dict[key] = val
    
    def eval(self, x):
        "Return value with given value of x"
        output = 0
        for key in self.dict.keys():
            if self.dict[key] != 0:
                val = self.dict[key] * (x ** key)
                output += val
        return output

    def deriv(self):
        output = Polynomial()
        for key in self.dict.keys():
            if key != 0:
                new_key = key - 1
                new_val = key * self.dict[key]
                output.dict[new_key] = new_val
        return output