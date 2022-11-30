// Copyright 2022 XingyuChen chxy517@bu.edu
// Copyright 2022 yilei feng fengyl@bu.edu


#include <iostream>
#include <string>

using namespace std;

int main() {
    string num;
    int base1;
    int base2;
    cin >> num;
    cin >> base1;
    cin >> base2;
    int number = 0;
    int weight = 1;
    for (int i = num.size() - 1; i >= 0; i--) {
        int digit = int(num[i]) - int('0');
        number += digit * weight;
        weight *= base1;
    }
    string output;
    while (number > 0) {
        int digit = number % base2;
        number = number / base2;
        output = char(digit + int('0')) + output;
    }
    cout << output;
    return 0;
}
