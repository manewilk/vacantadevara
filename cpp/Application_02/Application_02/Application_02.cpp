// Application_02.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int nrofzeros(int x) {
	int a, zcounter = 0;
	while (x>0) {
		a = x % 10;
		//std::cout << "A x este: " << x << "\n";
		x = x / 10;
		//std::cout << "B x este: " << x << "\n";
		if (a==0) {
			zcounter++;
		}
	}
	return zcounter;
}

//int main()
//{
//	int x, a, counter;
//	std::cout << "introduceti un numar: ";
//	std::cin >> x;
//	std::cout << "Ati introdus numarul " << x <<"\n";
//	counter = nrofzeros(x);
//	std::cout << "Counter is "<< counter <<"\n";
//	std::cout << "Game over";
//	return 0;
//}



int main()
{
	int x;
	int counter = 0;
	std::cout << "introduceti un numar: ";
	std::cin >> x;
	std::cout << "Ati introdus numarul " << x<<"\n";
	while (x != -1) {

		counter =  counter + nrofzeros(x);

		std::cout << "introduceti un numar: ";
		std::cin >> x;
		std::cout << "Ati introdus numarul " << x<<"\n";
	}
	std::cout << "Counter is "<< counter <<"\n";
	std::cout << "Game over";

	return 0;

}

