
#include "stdafx.h"
#include <iostream>
#include<string>
#include<sstream>
#include<cmath>
#include<ctime>
//Name: Michael Waldron
//Student ID: 100657864

using namespace std;

int main()
{
	bool win = false;
	// this is the variables for the range of how big the random num can be and the random number
	int range = 5;
	int k = rand() % range;
	// this the variable that will tell the player what round they are on
	int round = 1;
	cout << "Welcome to the Guessing Game";
	// for loop where x is the number of guesses the player makes and will exit if x is greater or equal to 5
	for (int x = 0; x < 5; x++) {
		// if the player won the last round than win will be true and x will be reset to 0
		if (win == true)x = 0;
		// variable that the users input guess is stored in
		int guess;
		cout << "\nGuess a number under " << range<<" you are currently playing round "<<round<<"\n";
		// this cin takes the users input and stores it in the guess variable
		cin >> guess;
		// the range doubles and the random variable is re created with the new range and the round variable increases
		if (guess == k) {
			cout << "Congrats you got it right proceed to the next round ";
			range = range * 2;
			k = rand() % range;
			round++;
			//resets the # of guesses
			win = true;
		}
		// if the guess is wrong the player gets an updated value of how many guesses he/she has left
		else {
			win = false;
			cout << "You got it wrong you have " << 5 - (x + 1) << " guess(es) left good luck ";
		}
	}
	cout << "\nThanks for playing you made it to round " << round;
    return 0;
}
