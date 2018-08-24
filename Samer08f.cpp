//http://www.spoj.com/problems/SAMER08F/
#include<iostream>
using namespace std;
int main()
{
  while(1)
  {
    int num;
    cin >> num;
    if(num == 0)
      break;
    int ans = num * (num + 1) * (2 * num + 1) / 6;
    cout << ans << endl;
  }
}