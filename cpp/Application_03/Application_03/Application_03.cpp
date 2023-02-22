// Application_03.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>
double f(double x,double y) {
	double res;
	if (x > 0 && y > 0) {
		res = (x + y) / (5 * x * y);
	}
	else if (x == 0 || y == 0) {
		res = std::min(x, y);
	}
	else {
		res = (pow(x, -1) + pow(y, -1)) *
			  (pow(x, -1) + pow(y, -1) +
				pow(x, 2) + pow(y, 2));
	}

	return res;
}

int main()
{
	double a, b;
	std::cout << "Introduceti doua numere: " << "\n";
	std::cin >> a;
	std::cin >> b;
	std::cout << "Rezultatul este: " << f(a, b);
	return 0;

	
}

