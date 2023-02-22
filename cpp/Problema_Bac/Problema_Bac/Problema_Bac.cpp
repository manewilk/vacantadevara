#include <iostream>

int f(int n) {
	if (n <= 2) return n;
	if (n % 2 == 1) return f(n - 2) - f(n - 1);
	return f(n - 1) - f(n - 2);
}


int main()
{
	std::cout << f(6);
	return 0;
}

