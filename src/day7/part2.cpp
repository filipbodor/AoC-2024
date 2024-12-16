#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <vector>
#include <sstream>
using namespace std;

struct Equation {
    long long num;
    vector<int> numbers;
};

vector<Equation> equations;

void setup() {
    ifstream file("../../inputs/day7.txt");
    if (!file.is_open()) return;

    string line;
    while (getline(file, line)) {
        std::stringstream ss(line);
        std::string keyPart, valuePart;

        std::getline(ss, keyPart, ':');
        std::getline(ss, valuePart); 

        Equation equation;

        equation.num = std::stoll(keyPart);

        std::stringstream valueStream(valuePart);
        int value;
        while (valueStream >> value) {
            equation.numbers.push_back(value);
        }

        equations.push_back(equation);
    }
}

int count(int n, int idx, long long subresult) {
    if (subresult > equations[n].num || idx == equations[n].numbers.size()) {
        return (subresult == equations[n].num);
    }
    
    if (count(n, idx + 1, subresult * equations[n].numbers[idx])) return 1;

    if (count(n, idx + 1, subresult + equations[n].numbers[idx])) return 1;
    
    int mul = 10;
    while (mul < equations[n].numbers[idx]) mul *= 10;

    return count(n, idx + 1, subresult * mul + equations[n].numbers[idx]);

}

void solve() {
    long long counter = 0;

    for (int i = 0; i < equations.size(); i++) {
        if (count(i, 0, 0)) {
            counter += equations[i].num;
        } 
    }

    cout << counter << endl;
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