#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <vector>
#include <sstream>
#include <map>
#include <set>
using namespace std;

typedef pair<int, int> pos;

set<pos> antinodes;
map<int, vector<pos>> antennas;
int height;
int width;

void setup() {
    ifstream file("../../inputs/day8.txt");
    if (!file.is_open()) return;

    int y, x = 0;
    string line;
    while (getline(file, line)) {
        for (int x = 0; x < line.size() && line[x] != '\n'; x++) {
            if (line[x] == '.') continue;

            if (antennas.find(line[x]) != antennas.end()) antennas[line[x]].push_back({x, y});
            else antennas[line[x]] = {{x, y}};

            antinodes.insert({x, y});
        }
        y++;
    }

    height = y;
    width = line.size();
}

void solve() {
    for (auto f : antennas) {
        for (int j = 0; j < f.second.size() - 1; j++) {
            for (int k = j + 1; k < f.second.size(); k++) {
                int vel_x = f.second[j].first - f.second[k].first;
                int vel_y = f.second[j].second - f.second[k].second;

                int i = 1;
                while (1) {
                    pos antinode = {f.second[j].first + (vel_x * i), f.second[j].second + (vel_y * i)};
                    if (antinode.first >= 0 && antinode.first < width && antinode.second >= 0 && antinode.second < height) antinodes.insert(antinode);
                    else break;
                    i++;
                }

                i = 1;
                while (1) {
                    pos antinode = {f.second[k].first - (vel_x * i), f.second[k].second - (vel_y * i)};
                    if (antinode.first >= 0 && antinode.first < width && antinode.second >= 0 && antinode.second < height) antinodes.insert(antinode);
                    else break;
                    i++;
                }
            }
        }
    }


    cout << antinodes.size() << endl;
}

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();

    setup();
    solve();
    
    auto end_time = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(end_time - start_time);
    cout << "Clock time: " << duration.count() / (double)1000000 << " s" << endl;

    return 0;
}