#include <iostream>
#include <vector>
#include <set>
#include <stdlib.h>
using namespace std;

bool duplicates(vector<int> &values)
{
	for each (int i in values)
	{
		int count = 0;
		for each (int j in values)
		{
			if (i == j)
			{
				count++;
			}
		}
		if (count > 1)
		{
			return true;
		}
	}

	return false;
}

int main()
{
	bool correctinput = false;
	// === print user instructions ======
	cout << "Enter a series of numbers, one at a time. " << endl;

	// === get user input ======
	vector<int> inputs;

		for (int i = 0; i < 5; i++)
		{
			int num;
			cin >> num;
			inputs.emplace_back(num);
		}


		// === confirm to the user what they entered ======
		cout << "You entered :";
		for (int i : inputs)
		{
			cout << i << ", ";
		}
		cout << endl;
		if (duplicates(inputs) == true)
		{
			cout <<"there are duplicates \n";
		}
		else
		{
			cout << "there are no duplicates \n";
		}
	return 0;
}