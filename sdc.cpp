#include<iostream>
#include<cmath>
#include<string>
using namespace std;

int sum_of_squares(long n)
{
  string s=to_string(n);
  int tot=0,i;
  for(i=0;i<s.length();i++)
  {
    tot+=pow((int)s[i]-int('0'),2);
  }
  return tot;
}

int main()
{
  int a[568];
  int i,tot=0;
  for(i=0;i<568;i++)
    a[i]=0;
  cout<<sum_of_squares(43)<<endl;
}
