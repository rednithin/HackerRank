#include<iostream>
using namespace std;
int main() 
{
	long long t;
	cin >> t;
	while(t--)
	{
		long long first, second, third;
		cin >> first >> second >> third;
		long long n = ( 2 * third ) / ( first + second ) ;
		long long d = 0;
		if(n-5 != 0)
			d = (second - first) / (n - 5);
		long long a = first - 2 * d;
		cout << n << endl;
		for(long long i = 0; i < n; i++)
		{
			cout << a << ' ';
			a += d;
		}
		cout << endl;
	}
	return 0;
}