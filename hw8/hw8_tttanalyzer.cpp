// Copyright 2022 XingyuChen chxy517@bu.edu

#include <iostream>
#include <string>
#include <array>
#include <vector>
#include <map>
#include "movedef.h"

using namespace std;

bool checkWinner(string board, int i, int j) {
    char cur = board.at(i * 3 + j);

    // Check row
    if (cur == board.at(i * 3 + (((j + 1) % 3) + 3) % 3) && cur == board.at(i * 3 + (((j - 1) % 3) + 3) % 3)) {
        return true;
    }

    // Check col
    if (cur == board.at(((((i + 1) % 3) + 3) % 3) * 3 + j) && cur == board.at(((((i - 1) % 3) + 3) % 3) * 3 + j)) {
        return true;
    }

    // Check cross
    if (i == j) {
        if (cur == board.at(((((i + 1) % 3) + 3) % 3) * 3 + (((j + 1) % 3) + 3) % 3) && cur == board.at(((((i - 1) % 3) + 3) % 3) * 3 + (((j - 1) % 3) + 3) % 3)) {
            return true;
        }
    } 
    else if (i + j == 2) {
        if (cur == board.at(((((i + 1) % 3) + 3) % 3) * 3 + (((j - 1) % 3) + 3) % 3) && cur == board.at(((((i - 1) % 3) + 3) % 3) * 3 + (((j + 1) % 3) + 3) % 3)) {
            return true;
        }
    }

    return false;
}

char tttresult(string board) {
    // Invalid board size
    if (board.size() != 9) {
        return 'e';
    }

    // Count number of spaces and symbols
    int x = 0;
    int o = 0;
    int space = 0;

    // Flags that show the winner
    int x_flag = 0;
    int o_flag = 0;

    // Loop through the board
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            int index = i * 3 + j;
            if (board.at(index) == '#') {
                space++;
            } 
            else if (board.at(index) == 'x') {
                x++;

                // If x is not winner yet, do the check
                if (x_flag == 0) {
                    if (checkWinner(board, i, j)) {
                        x_flag = 1;
                    }
                }
            }
            else if (board.at(index) == 'o') {
                o++;

                // If x is not winner yet, do the check
                if (o_flag == 0) {
                    if (checkWinner(board, i, j)) {
                        o_flag = 1;
                    }
                }
            }
            // Invalid char
            else {
                return 'e';
            }
        }
    }

    // Check unbalance number
    if (x - o > 1 || o > x) {
        return 'i';
    }

    if (x_flag == 1 & o_flag == 1) {
        return 'i';
    }
    else if (x_flag == 1 & o_flag == 0) {
        if (x == o) {
            return 'i';
        }
        else {
            return 'x';
        }
    }
    else if (x_flag == 0 & o_flag == 1) {
        if (x == o) {
            return 'o';
        }
        else {
            return 'i';
        }
    }
    else if (space == 0) {
        return 't';
    } 
    else {
        return 'c';
    }
}

char tttresult(vector<Move> board) {
    string s = "#########";

    for (int i = 0; i < board.size(); i++) {
        int index = board.at(i).r * 3 + board.at(i).c;
        
        // Row, Col size check && Player char check
        if (board.at(i).r > 2 || board.at(i).c > 2 || board.at(i).player != 'x' && board.at(i).player != 'o') {
            return 'e';
        }

        s.at(index) = board.at(i).player;

        // First player char check, consecutive players cannot be the same check
        if (i != board.size() - 1 && s.at(index) == board.at(i + 1).player || board.at(0).player != 'x') {
            return 'i';
        }
    }
    return tttresult(s);
}

void permutation(string& cur, vector<string>& result) {
    // Add to vector when current string is completed
    if (cur.size() == 9) {
        result.push_back(cur);
        return;
    }

    // Add '#' to current string
    cur.append("#");
    permutation(cur, result);
    cur.erase(cur.size() - 1);

    // Add 'x' to current string
    cur.append("x");
    permutation(cur, result);
    cur.erase(cur.size() - 1);

    // Add 'o' to current string
    cur.append("o");
    permutation(cur, result);
    cur.erase(cur.size() - 1);
}

vector<string> get_all_boards() {
    string cur;
    vector<string> result;
    permutation(cur, result);
    return result;
}

void ttt_tally() {
    int x_cnt = 0, o_cnt = 0, t_cnt = 0, i_cnt = 0, c_cnt = 0;
    vector<string> all_boards = get_all_boards();
    for (auto cur : all_boards) {
        switch(tttresult(cur)) {
            case 'x':
                x_cnt++;
                break;
            case 'o':
                o_cnt++;
                break;
            case 't':
                t_cnt++;
                break;
            case 'i':
                i_cnt++;
                break;
            case 'c':
                c_cnt++;
                break;
        }
    }
    cout << "x " << x_cnt << endl;
    cout << "o " << o_cnt << endl;
    cout << "t " << t_cnt << endl;
    cout << "i " << i_cnt << endl;
    cout << "c " << c_cnt << endl;
}

// MAIN

int main() {
    vector<Move> moves;
    bool error;
    char result;

    Move m; // make a move 
    m.r = 0; // fill the data
    m.c = 1;
    m.player = 'x';

    moves.push_back(m); // put the move on the vector representing the board.

    // result = tttresult(moves);  // returns 'c'
    // cout << result << endl;
    
    result = tttresult("####oxxxo"); // returns 'e'
    cout << result << endl;
}