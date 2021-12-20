// PROBLEM 47
#include <vector>
#include <iostream>
#include <set>
#include <iterator>
#include <algorithm>
#include<cmath>

// Returns a set of prime factors powered by their multiplicity. 
std::set<int> prime_factorizer(int n) {
	std::set<int> s;
	int rem = n;
	int x = 2;
	int x_previous = 0;
	int count = 1;
	while (x < rem + 1) {
		if (rem % x == 0) {
			rem = rem / x;
			if (x == x_previous) {
				count++;
			}
			else {
				s.insert(std::pow(x_previous, count));
				x_previous = x;
				count = 1;
			}
				
		} else { 
			x++;
		}
	}
	s.insert(std::pow(x_previous, count));
	s.erase(0);
	return s;
}

// Checks if the size of the union of the four sets is equal to the 4 individual sizes
bool check_sets(std::set<int> s1, std::set<int> s2, std::set<int> s3, std::set<int> s4) {
	int size = s1.size() + s2.size() + s3.size() + s4.size();
	if (size != 16) {
		return false;
	}
	std::set<int> u1, u2, u3;
	std::set_union(s1.begin(), s1.end(), s2.begin(), s2.end(),
		std::inserter(u1, u1.begin()));
	std::set_union(u1.begin(), u1.end(), s3.begin(), s3.end(),
		std::inserter(u2, u2.begin()));
	std::set_union(u2.begin(), u2.end(), s4.begin(), s4.end(),
		std::inserter(u3, u3.begin()));
	return size == u3.size();
}

std::set<int> ans1 = prime_factorizer(650);
std::set<int> ans2 = prime_factorizer(651);
std::set<int> ans3 = prime_factorizer(652);
int n = 653;
int main() {
	while (true) {
		std::set<int> ans4 = prime_factorizer(n);
		if (ans4.size() != 4) {
			ans1 = ans2;
			ans2 = ans3;
			ans3 = ans4;
			n++;
			continue;
		}

		// Check ifs the 4 sets are disjoint and all have length 4. 
		if (check_sets(ans1, ans2, ans3, ans4)) {
			std::cout << "Found: " << n - 3 << '\n';
			break;
		}

		ans1 = ans2;
		ans2 = ans3;
		ans3 = ans4;
		n++;
	}

	std::cout << " Done" << std::endl;
	std::getchar();
}
