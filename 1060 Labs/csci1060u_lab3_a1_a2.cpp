// ConsoleApplication5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include<string>
#include<sstream>
#include<cmath>
#include<ctime>
//Name: Michael Waldron
//Student ID: 100657864
//function prototypes
void swapper(int& a, int& b);
int* bubble(int a[], int size);
int randint();
using namespace std;
// creates a random integer between 0-9999
int randint() {
	int ran = rand() % 10000;
	return ran;
}
// uses pointers to directly swap the values in question
void swapper(int & a, int & b) {
	int c;
	c = a;
	a = b;
	b = c;
}

int* bubble(int a[], int size) {
	//sorting algorithm using bubble sort 
	for (int y = 0; y < size - 1; y++) {
		for (int x = 0; x < size - 1; x++) {
			if (a[x] > a[x + 1])
				swapper(a[x], a[x + 1]);
		}
	}
	// returns where the sorted array is located in the computers memory
	return a;
}

int main()
{ //part 2
	//variables for the list with 10000 and 1000 elements and pointer variables
	int m[10000];
	int n[1000];
	int *m1;
	int *n1;
//testing the list for the array with 1000 elements
	//creating the array with 1000 random elements
	for (int f = 0; f<1000; f++)n[f] = randint();
	//starting the timer for testing to see how long it takes to sort
	clock_t start_t = clock();
	n1=bubble(n, 1000);
	//stopping the timer after the sort finishes
	clock_t stop_t = clock();
	//out putting the time then a loop that outputs the sorted array
	cout << "it took : " << (float)(stop_t = start_t) / CLOCKS_PER_SEC << "s for the sorting algorithm to sort through 1000 elements here is the sorted array";
	for (int x = 0; x < 1000; x++) {
		cout << n1[x]<<" ";
	}
	cout << endl;
//testing the array with 10000 elements
	//creating the array with 10000 random elements
	for (int f = 0; f < 10000; f++)m[f] = randint();
	//starting the timer for testing to see how long it takes to sort
	clock_t start_t2 = clock();
	m1=bubble(m, 10000);
	//stopping the timer after the sort finishes
	clock_t stop_t2 = clock();
	//out putting the time then a loop that outputs the sorted array
	cout << "it took : " << (float)(stop_t = start_t) / CLOCKS_PER_SEC << "s for the sorting algorithm to sort through 10000 elements here is the sorted array";
	for (int x = 0; x < 1000; x++) {
		cout << m1[x] << " ";
	}
	cout << endl;
	//Part 1
	//initializing the array
	int d[5];
	//loop to take inputs from the user and store them in the array
	for (int x = 0; x < 5; x++) {
		cout << "please enter an integer ";
		cin >> d[x];
	}
	// storing the pointer of the sorted array to a pointer variable
	int* y = bubble(d, 5);
	//printing sorted array
	cout << "your sorted array is" << endl;
		for (int x = 0; x < 5; x++) {
			cout << d[x] << " ";
		}
	return 0;
}
