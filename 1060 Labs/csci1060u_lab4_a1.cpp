// ConsoleApplication7.cpp : Defines the entry point for the console application.
//Michael Waldron
//100657864

#include "stdafx.h"
#include <iostream>
#include<string>
#include<sstream>
#include<cmath>
#include<ctime>
#include <fstream>	
using namespace std;
string* bubble(string a[], int size);
string* bubble2( string a[], int size);
bool swapper(string& a, string& b);
bool swapper2( string a,  string b);
//swapping returns true if a swap is needed (by value)
bool swapper2( string a,  string b)
{
	if (a.length() > b.length()) {
		return true;
	}
	else return false;
}
//returns true if swap is needed and swaps values by refernce
bool swapper(string& a, string& b)
{
	if (a.length() > b.length()) {
		string c;
		c = a;
		a = b;
		b = c;
		return true;
	}
	else return false;
}
//call by value
string* bubble2(string a[], int size) {
	//sorting algorithm using bubble sort 
	for (int y = 0; y < size - 1; y++) {
		for (int x = 0; x < size - 1; x++) {
			
			if(swapper2(a[x],a[x+1])==true)
			{
				//actual swap is done here if swapper2(by value) returns true 
				string temp;
				temp = a[x];
				a[x] = a[x + 1];
				a[x + 1] = temp;
			}
		}
		// returns where the sorted array is located in the computers memory
		return a;
	}
}
//call by reference
string* bubble(string a[], int size) {
	//sorting algorithm using bubble sort 
	for (int y = 0; y < size - 1; y++) {
		for (int x = 0; x < size - 1; x++) {
			swapper(a[x], a[x + 1]);
		}
		// returns where the sorted array is located in the computers memory
		return a;
	}
}
int main()
{
	// opening the file reading the inputs making the array of strings, getting the user input etc
	ifstream is;
	string file;
	cout << "please type in the file name you wish to open";
	cin >> file;
	is.open(file);
	if (is.fail()) cout << "failed to open results are not accutate" << endl;
	string dd[1000];
	for (int i = 0; i<1000; i++)
	{
		if (is.peek() != EOF){
			is >> dd[i];
	 }
		else dd[i] = "";

	}
	//starting the timer for testing to see how long it takes to sort
	// call by reference
	clock_t start_t = clock();
	//storing the sorted array
	string* one1 = bubble(dd,1000);
	//stopping the timer after the sort finishes
	clock_t stop_t = clock();
	cout << "it took : " << (float)(stop_t = start_t) / CLOCKS_PER_SEC << "s for the sorting algorithm to sort through 1000 elements using call by reference here is the sorted array" << endl;
	/*for (int x = 0; x < 1000; x++) {
		cout << one1[x] << " ";
	}*/
	// for sorting using call by value
	clock_t start_t2 = clock();
	//storing the sorted array
	string* one2 = bubble2(dd, 1000);
	//stopping the timer after the sort finishes
	clock_t stop_t2 = clock();
	cout << "it took : " << (float)(stop_t2 = start_t2) / CLOCKS_PER_SEC << "s for the sorting algorithm to sort through 1000 elements using call by value here is the sorted array"<<endl;
	// uncomment if you wish to see the sorted array same with the one above
	/*for (int x = 0; x < 1000; x++) {
		cout << one2[x]<<" ";
	}*/
	// closing the file
	is.close();
    return 0;
}

