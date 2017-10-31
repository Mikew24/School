#include "iostream"
#include"string"
#include"sstream"
//Name: Michael Waldron
//Student ID: 100657864
using namespace std;
int main()
{
	//declaration of variables for storing the users data
	string name;
	string lname;
	int byear;
	double wage;
	// assigning the inputs of the user to the corresponding variables
	cout << "pleae type in your first name\n";
	cin >> name;
	cout << "please type in your last name\n";
	cin >> lname;
	cout << "please type in your birth year\n";
	cin >> byear;
	cout << "please type in your hourly wage\n";
	cin >> wage;
	//outputting and lableing the users data line by line
	cout << "First Name:" << name << "\nLast Name: " << lname
		<< "\nBirth Year:" << byear << "\nHourly Wage: " << wage;
	// putting the users data into a coherent sentence
	cout << "\n" << name << " " << lname << " is " << 2017 - byear << " years old and request a hourly wage of $" << wage << "\n";
	// this cin is to keep the console open
	cin >> name;
	return 0;
}