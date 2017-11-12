#include "stdafx.h"
#include <cmath>
#include<iostream>
#include <string>
#include <functional>
const int months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
const std::string days[7] = { " S"," M","Tu"," W"," T"," F","Sa" };
using namespace std;
int day(int year, int month);
void printMonth(int year, int month);
void printMonth(int year, int month)
{
	// get the first day of the month
	bool firstday = false;
	int dayn = 1;
	int weekday = day(year, month);
	int daysInMonth;
	if (month == 2 && year % 4 == 0 || year % 100 == 0 && year % 400 == 0 && month == 2)
	{
		daysInMonth = 29;
	}
	else daysInMonth = months[month-1];

	string calendar[7][6];
	string startingDay = days[weekday];
	for (int x = 0; x < 7; x++)
	{
		calendar[0][x] = days[x];
		string d = calendar[0][x];
		cout << d<<" ";
	}
	for(int x = 1; x<7;x++)
	{
		cout << endl;
		for(int y = 0;y<6;y++)
		{
			if (calendar[0][y] == startingDay)firstday = true;
			else {
				calendar[x][y] = "  ";
				cout << calendar[x][y];
			}
			if (firstday == true&&daysInMonth>=dayn) {
				string date = to_string(dayn);
				if (date.length() < 2) date = " " + date;
				calendar[x][y] = date;
				cout << calendar[x][y] +" ";
				dayn++;
			}
		}
	}
	/*for(int x = 0; x<7;x++)
	{
		cout << endl;
		for(int y = 0;y<6;y++)
		{
			cout<<
		}
	}*/
}
int day(int year, int month)
{
	int weekday;
	int day = 1;
	int century = year / 100;
	int Y = year % 100;
	if(month!=1 &&month!=2)
	{
		month = month - 2;
	}
	else
	{	
		if (month == 1)month = 11;
		if (month == 2)month = 12;
	}
	weekday =(day + floor(2.6*month - 0.2) - 2 * century + Y + floor(Y / 4) + floor(century/4));
	weekday = weekday % 7;
	if (weekday < 0)weekday = weekday + 7;
	return weekday;
}
int main()
{
	cout<<day(2017 ,12);
	printMonth(2017, 5);
    return 0;
}
