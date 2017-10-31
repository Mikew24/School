#include "iostream"
#include"string"
#include"sstream"
//Name: Michael Waldron
//Student ID: 100657864

using namespace std;
	int main()
	{
		//part 2 
		//assigning the course code to a variable
		string course = "CSCI 1060U";
		// a temp int named f to store eacha asci value of the characters in the course string
		int f;
		//a loop for converting characters to asci and outputting them to the console
		cout << "the asci code for " << course << " is ";
		for (int x = 0; x < course.length(); x++) {
			f = (int) course.at(x);
			cout << f;
		}
		// this cin is here to keep the console open
		cin >> f;
		
		return 0;
	}