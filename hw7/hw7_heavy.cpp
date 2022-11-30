// Copyright 2022 XingyuChen chxy517@bu.edu
// Copyright 2022 yilei feng fengyl@bu.edu

#include <vector>
#include <string>

using std::string;
using std::vector;
using std::stoi;

string convertbase(int num, int tobase) {
    // Convert num from base 10 to base 'tobase'
    if (num == 0)
        return "0";
    string output;
    while (num > 0) {
        int digit = num % tobase;
        num = num / tobase;
        output = char(digit + int('0')) + output;
    }
    return output;
}

int main(int argc, char **argv) {
    int num = stoi(argv[1]);
    int base = stoi(argv[2]);
    string converted_num = convertbase(num, base);
    vector<string> visited;
    while (true) {
        int sqr_sum = 0;
        for (int i = 0; i < converted_num.length(); i++) {
            sqr_sum += (converted_num.at(i) - '0') * (converted_num.at(i) - '0');
        }
        converted_num = convertbase(sqr_sum, base);

        // Found heavy number! Return 1
        if (converted_num == "1") {
            return 1;           
        }
        
        // Search converted_num in visited, if exist return 0
        for (int i = 0; i < visited.size(); i++) {
            if (converted_num == visited.at(i)) {
                return 0;
            }
        }

        // else add converted_num to the list
        visited.push_back(converted_num);
    }
    return 0;
}