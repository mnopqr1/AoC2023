#include <iostream>
#include <fstream>
#include <cctype>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

const string digits[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

/* Returns the digit whose name is found in str when starting to read from pos, or -1 if 
   there is none. */
int digitname(const string str, size_t pos) {
    for (int d = 0; d < 10; d++) {
            if (str.substr(pos, digits[d].length()) == digits[d]) return d;
        }
    return -1;
}

/* Returns the first occurrence of a digit in a string, or the last, if `reverse` is true. 
   If `includenames` is true, the name of a digit is also counted as a digit. */
int firstdigit(const string str, bool reverse, bool includenames) {
    size_t initpos = reverse ? str.length() - 1 : 0;
    int inc = reverse ? -1 : 1;
    int res = -1;
    for (size_t pos = initpos; 0 <= pos && pos < str.length(); pos += inc) {
        if (isdigit(str[pos])) return str[pos] - '0';
        if (includenames && (res = digitname(str, pos)) != -1) return res;
    }
    return 0;
}

/* Computes the sum of numbers found in each line. */
int main() 
{
    std::ifstream infile("input.txt");
    string line;
    int total = 0;
    const bool part2 = true;

    while (getline(infile, line)) 
        {
            total += 10 * firstdigit(line, false, part2) + firstdigit(line, true, part2);
        }
        cout << total << "\n";
}
