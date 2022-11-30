// Copyright 2022 XingyuChen chxy517@bu.edu

#include <iostream>
#include <cstdint>

using namespace std;

int main() {
    int num;
    while (true) {
        unsigned long sum = 1;
        cin >> num;
        if (num == 0) {
            break;
        }
        cout << num << ": 1";
        for (int i = 2; i < num / 2 + 1; i++) 
        {
            if (num % i == 0) 
            {
                sum += i;
                cout << "+" << i;
            };
        };
        cout << " = " << sum << "\n"; 
    }   
    return 0;
}