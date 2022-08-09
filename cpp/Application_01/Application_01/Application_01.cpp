// Application_01.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdio.h>
#include <cmath>

int main()
{
	int n;
	std::cout << "Introduceti un numar: ";
	std::cin >> n;
	for (int i = 1; i*i < n; i++) {
		std::cout << i*i << "\n";

	}


return 0;
}

