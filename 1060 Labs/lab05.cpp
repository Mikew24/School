/******************************************************************************************
 *Name/Student #: Michael Waldron/100657864
 *Version #: 1.1
 *Purpose:For the user to have a visual reference of how many units each factory is producing
 *How to Execute: Nothing special just run 
 *Expected Input/Output: input the units per department of each factory/output will be sum/factory and (sum/1000)/factory via '*'
 ********************************************************************************************/

#include <iostream> // allows the console to output data and take user input
#include <cmath>// imports various math function in this program the round function is used

using namespace std;// allow user accsess to the standard namespace without using the 'std::' prefix

const int kFactor = 3;// number of factorys involved (cant be changed)

// method declaration
void productionData(int a[], int aNumber);// asks user for prduction data then calls the prodSumperFacotry method
void unitsInThousands(int a[], int anotherNumber);// outputs the number of units in thousands
void visualDataOrganizer(const int anArray[], int aNumber); // tells us what visual data belongs to what factoru
void prodSumPerFactory(int& sum); // takes user input and calculates the sum of units produced out of all the departments in a factory
int  roundDouble(double number); //rounds a double either up or down and casts into a type integer
void productionVisualData(int n);// represents the amount of units produced per factory by out putting asterisks (*==1000 units)

int main()
{
	int production[kFactor];// array for storing the units prodced per facory. Its size is equal to # of factorys
	cout << "This program displays a graph showing\n" 
		 << "production for each factory in the company.\n";
	
	productionData(production, kFactor);
	unitsInThousands(production, kFactor);

	return 0;
}

void productionData(int a[], int aNumber)
{	// loops through the factorys and calls a prodSumPerFactory to store its production data in the production arrau
	for (int factoryNum = 1; factoryNum <= aNumber; factoryNum++)
	{
		cout << endl << "Enter production data for plant number " << factoryNum << endl;
		prodSumPerFactory(a[factoryNum - 1]);
	}
}

void prodSumPerFactory(int& sum)
{
	// takes user input and adds it to the units produced sum and when a negative integer is input the loop ends and the sum is stored
	//using a reference pointer to ensure its stored in the production array
	cout << "Enter number of units produced by each department.\n"
	     << "Append a negative number to the end of the list.\n";
	sum = 0; 
	int next;
	cin >> next;
	while (next >= 0) {
		sum = sum + next;
		cin >> next;
	} 
	cout << "Total = " << sum << endl;
}

void unitsInThousands(int factoryArray[], int numberFactorys)
{
	// loops through the factories and divides the sum of each by 1000 then rounds to a whole integer and stores it in the factory array
	// then calls visualDataOrganizer using the copy of the production array with the units connverted to thousands of units
	for (int index = 0; index < numberFactorys; index++)
		factoryArray[index] = roundDouble(factoryArray[index] / 1000.0);
	visualDataOrganizer(factoryArray, numberFactorys);
}

int roundDouble(double number)
{
	//rounds to nearest whole number and converts it to a integer
	return static_cast<int>(floor(number + 0.5));
}

void visualDataOrganizer(const int factoryArray[], int numberFactorys)
{
	// outputs the factory number and then loops through the factorys and calls the visualData method
	cout << "\nUnits produced in thousands of units:\n";
	for (int factoryNum = 1; factoryNum <= numberFactorys; factoryNum++)
	{
		cout << "Factory #" << factoryNum << " ";
		productionVisualData(factoryArray[factoryNum-1]);
		cout << endl;
	}
}

void productionVisualData(int unitsInThousands)
{
	// outputs a '*' for each thousands of units *==1000 units
	for (int count = 1; count <= unitsInThousands; count++)
		cout << "*";
}

