# Copyright 2022 XingyuChen chxy517@bu.edu
# Copyright 2022 Xingjian(Oscar) Zhang zhangzxj@bu.edu
# Copyright 2022 Zhenghao Sun szh1007@bu.edu

class Wedding: 
    def __init__(self):
        pass

    def shuffle(self, guests):
        list = []
        if len(guests) == 1:
            return [guests[0]]
        if len(guests) == 0:
            return None
        if len(guests) == 2:
            a = guests
            b = guests[1] + guests[0]
            list.append(a)
            list.append(b)
            return list
    
        shuffle_recursion(list, guests, 0, '')

        return list
         
    def barriers(self, guests, bars):
        if len(guests) == 1:
            if (0 in bars):
                return ['|' + guests[0]]
            else:
                return [guests[0]]
        if len(guests) == 0:
            return None
    
        list = []
        barriers_recursion(list, guests, bars, 0, '')

        return list


def shuffle_recursion(list, guests, index, cur):
    # string has been constructed
    if (index == len(guests)):
        list.append(cur)
        return
        
    # 1. Left Neighbor
    left_char = guests[(index - 1) % len(guests)]
    if left_char not in cur:
        cur += left_char
        shuffle_recursion(list, guests, index + 1, cur)
        cur = cur[0:index]

    # 2. Original Char
    orig_char = guests[index]
    if orig_char not in cur:
        cur += orig_char
        shuffle_recursion(list, guests, index + 1, cur)
        cur = cur[0:index]

    # 3. Right Neighbor
    right_char = guests[(index + 1) % len(guests)]
    if right_char not in cur:
        cur += right_char
        shuffle_recursion(list, guests, index + 1, cur)
        cur = cur[0:index]

def barriers_recursion(list, guests, bars, index, cur):
    # string has been constructed
    if (index == len(guests)):
        list.append(cur)
        return
    
    # No bar on left or right
    if (index % len(guests) not in bars) and ((index + 1) % len(guests) not in bars):
        # 1. Left Neighbor
        left_char = guests[(index - 1) % len(guests)]
        if left_char not in cur:
            cur += left_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 1]

        # 2. Original Char
        orig_char = guests[index]
        if orig_char not in cur:
            cur += orig_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 1]

        # 3. Right Neighbor
        right_char = guests[(index + 1) % len(guests)]
        if right_char not in cur:
            cur += right_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 1]

    # Bar on both left and right
    elif (index % len(guests) in bars) and ((index + 1) % len(guests) in bars):
        # 1. Original Char
        orig_char = guests[index]
        if orig_char not in cur:
            cur += '|' + orig_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 2]

    # Bar on the left
    elif index % len(guests) in bars:
        # 1. Original Char
        orig_char = guests[index]
        if orig_char not in cur:
            cur += '|' + orig_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 2]

        # 2. Right Neighbor
        right_char = guests[(index + 1) % len(guests)]
        if right_char not in cur:
            cur += '|' + right_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 2]

    # Bar on the right
    else:
        # 1. Left Neighbor
        left_char = guests[(index - 1) % len(guests)]
        if left_char not in cur:
            cur += left_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 1]

        # 2. Original Char
        orig_char = guests[index]
        if orig_char not in cur:
            cur += orig_char
            barriers_recursion(list, guests, bars, index + 1, cur)
            cur = cur[0:len(cur) - 1]

# Template
def  show_result(v, partial=False,ind=None):
  v.sort()
  if not partial:
    print(len(v),"\n".join(v),sep="\n")
  else:
    print(len(v),v[ind],sep="\n")




def standard_tests():
  standard = Wedding()
  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("WXYZ")
  show_result(res)

  res = standard.barriers("xyz", [0])
  show_result(res)

  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("abcdefXY")
  show_result(res)

  res = standard.barriers("abcDEFxyz", [2, 5, 7])
  show_result(res)

  res = standard.barriers("ABCDef", [4])
  show_result(res)

  res = standard.barriers("bgywqa", [0, 1, 2, 4, 5])
  show_result(res)

  res = standard.barriers("n", [0])
  show_result(res)
  res = standard.shuffle("hi")
  show_result(res)



def main():

  print("""Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
""")
  w = Wedding()
  while True:
    asktype=input().split()
    if not asktype or asktype[0] == "quit":
      break;
    elif asktype[0] == "tests":
      standard_tests()
    elif asktype[0] == "s":
      guests = asktype[1]
      r = w.shuffle(guests)
      show_result(r);
    elif asktype[0] == "b":
      guests,nbar,bars = asktype[1],asktype[2],asktype[3:]
      r = w.barriers(guests, [int(x) for x in bars])
      show_result(r)
    elif asktype[0] == "sp":
      guests,ind = asktype[1:]
      r = w.shuffle(guests);
      show_result(r, True, int(ind));
    elif asktype[0] == "bp":
      guests,nbar,bars,ind  = asktype[1],asktype[2],asktype[3:-1],asktype[-1]
      r = w.barriers(guests, [int(x) for x in bars])
      show_result(r, True, int(ind))
    

if __name__ == '__main__':
  main()