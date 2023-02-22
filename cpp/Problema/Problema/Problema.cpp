#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;


int main()
{
    int a[4][4], b[4][4];
    int i, j;

    FILE *file;
    file = fopen("D:/Coding_vacanta_de_vara/vacantadevara/cpp/Problema/problema/problema.txt", "rb");
    // read the input file
    puts("read the input file");

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if (!fscanf(file, "%u", &a[i][j])) {
                break;  
            }
            printf("%u\t", a[i][j]);
        }
        printf("\n");
    }
    fclose(file);

    // get binary matrix
    puts("get binary matrix");

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {

            if (a[i][j]%3==0) {
                b[i][j] = 1;
            }
            else {
                b[i][j] = 0;
            }

            printf("%u\t", b[i][j]);
        }
        printf("\n");
    }
    // save b to file
    puts("save b to file");

    fstream myfile;
    myfile.open("D:/Coding_vacanta_de_vara/vacantadevara/cpp/Problema/Problema/output_problema.txt", fstream::out);
    
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            myfile << b[i][j] << "\t";
        }
        myfile << std::endl;
    }

    
    myfile.close();
    return 0;
}

