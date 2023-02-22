// Application_o4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>



int main()
{
	int n;
	char T[20][20];
	std::cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j<n;j++){
			if (j < i) {
				T[i][j] = 'Q';
			}
			else {
				T[i][j] = 'O';
			}
			
			std::cout << T[i][j] << "\t";
			

		}
		std::cout << "\n";
	}
	
	
	
}


