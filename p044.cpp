#include <vector>
#include <iostream>
#include <algorithm>
// Problem 44

int pentagonal(int n) {
	int res = n * (3*n - 1) / 2;
	return res;
}

int size = 10000;
int D_lowest = 100000000;

int main() {
	std::vector<int> p;

	// Vector Creation
	for (int x = 1; x < size; x++) {
		int num = pentagonal(x);
		p.push_back(num);
	}

	// Looping through list and comparing with all values above
	for (int i1 = 0; i1 < size - 1; i1++) {
		for (int i2 = i1 + 1; i2 < size - 1; i2++) {
			int res1 = p[i2] - p[i1];
			int res2 = p[i2] + p[i1];
			if (std::find(p.begin(), p.end(), res1) != p.end() && std::find(p.begin(), p.end(), res2) != p.end()) {
				if (res1 < D_lowest) {
					D_lowest = res1;
					std::cout<<res1<<" "<<p[i1]<<" "<<p[i2]<<std::endl;
				}
			}
		}
	}
	
	std::cout << D_lowest << " Done" << std::endl;
	std::getchar();
}
