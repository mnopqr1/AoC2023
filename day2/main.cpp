#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>

using namespace std;

struct Draw { int r; int g; int b; };

bool possible(list<Draw> &game) {
    for (const Draw& v : game)
        if (v.r > 12 || v.g > 13 || v.b > 14) return false;
    return true;
}

int power(list<Draw> &game) {
    Draw vmax{0, 0, 0};
    for (const Draw& v : game) {
        if (v.r > vmax.r) vmax.r = v.r;
        if (v.b > vmax.b) vmax.b = v.b;
        if (v.g > vmax.g) vmax.g = v.g;
    }
    return vmax.r * vmax.g * vmax.b;
}

void trim(string& s) {
    while (!s.empty() && s[0] == ' ') s.erase(0,1);
}

void parseline(const string& line, list<Draw>& game, int& game_id) {
    string name = line.substr(0, line.find(':'));
    string content = line.substr(line.find(':')+2);
    game_id = stoi(name.substr(name.find(' ')+1));

    stringstream ss(content);
    string s;
    while (getline(ss, s, ';')) {
        Draw v{0, 0, 0};
        stringstream is(s);
        string c;
        while (getline(is, c, ',')) {
            trim(c);
            int n = stoi(c.substr(0,c.find(' ')));
            string col = c.substr(c.find(' ')+1);
            if (!col.empty() && col.back() == '\n') col.pop_back();
            if (col == "red") v.r = n;
            if (col == "green") v.g = n;
            if (col == "blue") v.b = n;
        }
        game.emplace_back(v); 
    }
}

int main() {
    ifstream infile("input.txt");
    string line;
    int total1 = 0;
    int total2 = 0;
    while (getline(infile,line)) {
        list<Draw> game;
        int game_id;
        parseline(line, game, game_id);
        if (possible(game)) {
            total1 += game_id;
        }
        total2 += power(game);
    }
    cout << total1 << endl;
    cout << total2 << endl;
}