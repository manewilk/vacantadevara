// ConsoleApplication0_4.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
int main()
{
    std::ifstream f("bac.txt");

    int a, previous = -1, max = -1;


    while (f >> a) {
        if (previous == a || max < a) {
            std::cout << a << "\n";
            previous = a;
            max = a;

        }
        else {
            previous = -1;
        }

 
    }

    return 0;
}

