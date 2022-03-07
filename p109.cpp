// PROBLEM 47
#include <iostream>
#include <cmath>
#include <vector>

// Array contains all possible dart throws, ordered from singles to triples
int all_throws[62] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 50, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60 };
int BORDER = 100;

// Each function returns all possible combinations when the last throw is at index i in [21, 41] in all_throws. 
// By doing this we fix the last throw and check all compatible throws such that the total is below the BORDER value.
int valid_2t(int index) {   // checks combinations with 2 throws
	int counter = 0;
	for (int i = 0; i < 62; i++) {
		if (all_throws[index] + all_throws[i] < BORDER) {
			counter++;
		}
	}
	return counter;
};

int valid_3t_3s(int index) { // checks combinations with 3 throws which are all separate
	int counter = 0;
	for (int i = 0; i < 62; i++) {
		if (index == i) {
			continue;
		}
		for (int j = i + 1; j < 62; j++) {
			if (index == j || i == j) {
				continue;
			}
			if (all_throws[index] + all_throws[i] + all_throws[j] < BORDER) {
				counter++;
			}
		}
	}
	return counter;
}

int valid_3t_1s(int index) { // checks combinations with 3 throws which are all the same
	int counter = 0;
	if (3 * all_throws[index] < BORDER) {
		counter++;
	}
	return counter;
}

int valid_3t_2s_nl(int index) {// checks 3 throw combinations where the first two throws are the same
	int counter = 0;
	for (int i = 0; i < 62; i++) {
		if (index == i) {
			continue;
		}
		if (all_throws[index] + 2 * all_throws[i] < BORDER) {
			counter++;
		}
	}
	return counter;
}

int valid_3t_2s_l(int index) {// checks 3 throw combinations where the last two throws are the same
	int counter = 0;
	for (int i = 0; i < 62; i++) {
		if (index == i) {
			continue;
		}
		if (2*all_throws[index] + all_throws[i] < BORDER) {
			counter++;
		}
	}
	return counter;
}

int main() {
	// Single throw count 
	int total = 21;

	// Double throw count
	for (int i = 0; i < 21; i++) {
		total += valid_2t(i + 21);
	}

	// Triple throw count
	for (int i = 0; i < 21; i++) {
		total += valid_3t_3s(i + 21);
		total += valid_3t_1s(i + 21);
		total += valid_3t_2s_l(i + 21);
		total += valid_3t_2s_nl(i + 21);
	}
	
	std::cout << total << std::endl;
	std::getchar();
}
