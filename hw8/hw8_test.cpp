#include <iostream>
#include <string>
#include <array>
#include <vector>

using namespace std;

int main() {
    vector<string> test;
    for (int i = 0; i < 399; i++) {
        test.push_back("first");
    }   
    int cnt = 0;
    for (std::vector<string>::iterator it = test.begin(); it != test.end(); it++) {
        cout << cnt << endl;
        cnt++;
    }
    cout << cnt << endl;
}