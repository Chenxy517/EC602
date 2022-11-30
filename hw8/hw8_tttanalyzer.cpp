#include <iostream>
#include <string>
#include <array>
#include <vector>
#include <map>
#include "movedef.h"

using namespace std;

bool checkWinner(char board[3][3], int i, int j) {
    char cur = board[i][j];

    // Check row
    if ((cur == board[i][(((j + 1) % 3) + 3) % 3]) && (cur == board[i][(((j - 1) % 3) + 3) % 3]) && (board[i][(((j + 1) % 3) + 3) % 3] == board[i][(((j - 1) % 3) + 3) % 3])) {
        return true;
    }

    // Check col
    if ((cur == board[(((i + 1) % 3) + 3) % 3][j]) && (cur == board[(((i - 1) % 3) + 3) % 3][j]) && (board[(((i + 1) % 3) + 3) % 3][j] == board[(((i - 1) % 3) + 3) % 3][j])) {
        return true;
    }

    // Check cross
    if (i == j) {
        if ((cur == board[(((i + 1) % 3) + 3) % 3][(((j + 1) % 3) + 3) % 3]) && (cur == board[(((i - 1) % 3) + 3) % 3][(((j - 1) % 3) + 3) % 3]) && (board[(((i + 1) % 3) + 3) % 3][(((j + 1) % 3) + 3) % 3] == board[(((i - 1) % 3) + 3) % 3][(((j - 1) % 3) + 3) % 3])) {
            return true;
        }
    } 
    else if (i + j == 2) {
        if ((cur == board[(((i + 1) % 3) + 3) % 3][(((j - 1) % 3) + 3) % 3]) && (cur == board[(((i - 1) % 3) + 3) % 3][(((j + 1) % 3) + 3) % 3]) && (board[(((i + 1) % 3) + 3) % 3][(((j - 1) % 3) + 3) % 3] == board[(((i - 1) % 3) + 3) % 3][(((j + 1) % 3) + 3) % 3])) {
            return true;
        }
    }

    return false;
}

char tttresult(string tttboard) {
    // Invalid board size
    if (tttboard.size() != 9) {
        return 'e';
    }

    // Convert string to char array
    char board[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = tttboard[i * 3 + j];
        }
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
            if (board[i][j] == '#') {
                space++;
            } 
            else if (board[i][j] == 'x') {
                x++;

                // If x is not winner yet, do the check
                if (x_flag == 0) {
                    if (checkWinner(board, i, j)) {
                        x_flag = 1;
                    }
                }
            }
            else if (board[i][j] == 'o') {
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
    if (x - o > 1 || o - x > 1) {
        return 'i';
    }

    if (x_flag == 1 & o_flag == 1) {
        return 'i';
    }
    else if (x_flag == 1 & o_flag == 0) {
        return 'x';
    }
    else if (x_flag == 0 & o_flag == 1) {
        return 'o';
    }
    else if (space == 0) {
        return 't';
    } 
    else {
        return 'c';
    }
}

char tttresult(vector<Move> board) {
    // initialize game board
    char gameboard[3][3];
    int x = 0;
    int o = 0;
    
    // Flags that show the winner
    int x_flag = 0;
    int o_flag = 0;

    for (vector<Move>::iterator cur = board.begin(); cur != board.end(); cur++) {
        int row = (*cur).r;
        int col = (*cur).c;

        if ((*cur).player == 'x') {
            gameboard[row][col] = 'x';
            x++;

            // Check round order
            if (x - o > 1) {
                return 'i';
            }

            // Check winner
            if (x_flag == 0) {
                if (checkWinner(gameboard, row, col)) {
                    x_flag = 1;
                }
            }
        }
        else if ((*cur).player == 'o') {
            gameboard[row][col] = 'o';
            o++;

            // Check round order
            if (o - x > 1) {
                return 'i';
            }

            // Check winner
            if (o_flag == 0) {
                if (checkWinner(gameboard, row, col)) {
                    o_flag = 1;
                }
            }
        }
        else {
            return 'i';
        }
    }

    if (x_flag == 1 & o_flag == 1) {
        return 'i';
    }
    else if (x_flag == 1 & o_flag == 0) {
        return 'x';
    }
    else if (x_flag == 0 & o_flag == 1) {
        return 'o';
    }
    else if (board.size() == 9) {
        return 't';
    } 
    else {
        return 'c';
    }
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
    cout << "o "  << o_cnt << endl;
    cout << "t " << t_cnt << endl;
    cout << "i " << i_cnt << endl;
    cout << "c " << c_cnt << endl;
}

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