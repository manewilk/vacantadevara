#include <iostream>

int f1(int n) {
	if (n == 0) return 1;
	return n * f1(n - 1);
}




int main()
{
	std::cout<<f1(12);

}