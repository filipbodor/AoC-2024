#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <vector>
#include <sstream>
#include <map>
#include <set>
using namespace std;

struct Space {
    int value;
    int position;
    int count;
};

vector<Space> fileSpaces;
vector<Space> freeSpaces;

void setup() {
    ifstream file("../../inputs/day9.txt");
    if (!file.is_open()) return;

    int position = 0;
    string line;
    getline(file, line);

    for (int i = 0; i < line.size(); i++) {
        Space space;
        space.value = i / 2;
        space.position = position;
        space.count = line[i] - '0';

        if (i % 2 == 0) fileSpaces.push_back(space);
        else freeSpaces.push_back(space);

        position += space.count;
    }
}

void solve() {
    long long checksum = 0;
    int fileIdx = fileSpaces.size() - 1;
    bool flag = true;

    for (int freeIdx = 0; freeIdx < freeSpaces.size() && flag; freeIdx++) {
        for (int i = 0; i < freeSpaces[freeIdx].count; i++) {
            if (fileSpaces[fileIdx].position < freeSpaces[freeIdx].position + i) {
                flag = false;
                break;
            }
            checksum += (freeSpaces[freeIdx].position + i) * fileSpaces[fileIdx].value;

            fileSpaces[fileIdx].count--;
            if (fileSpaces[fileIdx].count == 0) fileIdx--;
        }
    }
    fileIdx = 0;
    while (fileSpaces[fileIdx].count != 0) {
        for (int i = 0; i < fileSpaces[fileIdx].count; i++) {
            checksum += (fileSpaces[fileIdx].position + i) * fileSpaces[fileIdx].value;
        }
        fileIdx++;
    }

    cout << checksum << endl;
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