#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

bool search_string(string text, string substr)
{
	stringstream ss(text);
	string items;
	vector<string> tokens;
	while (getline(ss, items,' ')) {
		tokens.push_back(items);
	}
	for (int i = 0; i < tokens.size(); i++)
	{
		if (tokens[i] == substr)
		{
			return true;
		}
	}

	return false;
}

int main()
{
	int errflg = 1;
	string text = "This is the big piece of text that we are going to be searching in";

	if (search_string(text, "This") != true)
	{
		cerr << "Failed \"This\" test." << endl;
	}
	else if (search_string(text, "big") != true)
	{
		cerr << "Failed \"big\" test." << endl;
	}
	else if (search_string(text, "in") != true)
	{
		cerr << "Failed \"in\" test." << endl;
	}
	else if (search_string(text, "kermit") == true)
	{
		cerr << "Failed \"kermit\" test." << endl;
	}
	else
	{
		cout << "Passed all tests." << endl;
		errflg = 0;
	}

	return errflg;
}