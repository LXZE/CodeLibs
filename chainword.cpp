#include <iostream>
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
using namespace std;
int main()
{
	int l;
	int n;
	int err;
	string in;
	string x;
	cin >> l;
	cin >> n;
	forn(i,n){
		cin >> x;
		if(i==0) in = x;
		forn(j,l){
			if(x[j]!=in[j]) err++;
			if(err>2) break;
		}
		if(err<=2) in = x;
		err = 0;
	}
	cout << in;
	return 0;
}