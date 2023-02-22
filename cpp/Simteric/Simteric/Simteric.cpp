// Simteric.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int main()
{

	int a[21][21];
	int m, n;
	std::cout << "Introduceti un numar m = " << "\n";
	std::cin >> m;
	std::cout << "Introduceti un numar n = " << "\n";
	std::cin >> n;
	int simetric=1;
	for (int i = 0; i < m; i++) {
	for (int j = 0; j < n; j++) {
		std::cout << "Introduceti un element din matricea a... " << "\n";
		std::cin >> a[i][j];
	}
	}
	for (int i = 0; i < m; i++) {
		std::cout << "\n";
		for (int j = 0; j < (n-1)/2; j++) {
			std::cout << a[i][j] << " VS "<< a[i][n-j-1] << "\n";\
				if (a[i][j] != a[i][n - j - 1]) {
					simetric = 0;
			}
		}
	}
	if (simetric == 0) {
		std::cout << "Nu";
	}
	else {
		std::cout << "Da";
	}
}