#include <iostream>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;
int charToInt(char in) { return in-'0'; }
int main()
{
	char in,a,b;
	map<char,int*> var;
	do{
		cin >> in;
		switch(in){
			case '=': { cin >> a >> b; var[a] = new int; *var[a] = charToInt(b); break;}
			case '#': { cin >> a; cout << *var[a] << endl; break; }
			case '+': { cin >> a >> b; *var[a] += *var[b]; break; }
			case '-': { cin >> a >> b; *var[a] -= *var[b]; break; }
			case '*': { cin >> a >> b; *var[a] *= *var[b]; break; }
			case '/': { cin >> a >> b; *var[a] /= *var[b]; break; }
			case '!': { cout <<'!'; break; }
		}
	}while(in!='!');
}