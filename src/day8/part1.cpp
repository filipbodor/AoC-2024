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
        }
        y++;
    }

    height = y;
    width = line.size();
}

void solve() {
    set<pos> antinodes;

    for (auto f : antennas) {
        for (int j = 0; j < f.second.size() - 1; j++) {
            for (int k = j + 1; k < f.second.size(); k++) {
                int vel_x = f.second[j].first - f.second[k].first;
                int vel_y = f.second[j].second - f.second[k].second;

                pos antinode1 = {f.second[j].first + vel_x, f.second[j].second + vel_y};
                pos antinode2 = {f.second[k].first - vel_x, f.second[k].second - vel_y};

                if (antinode1.first >= 0 && antinode1.first < width && antinode1.second >= 0 && antinode1.second < height) antinodes.insert(antinode1);
                if (antinode2.first >= 0 && antinode2.first < width && antinode2.second >= 0 && antinode2.second < height) antinodes.insert(antinode2);
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