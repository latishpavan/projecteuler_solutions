#include<iostream>
using namespace std;

int main()
{
    int coins[]={1,2,5,10,20,50,100,200};
    int n=200;
    long total[8][n+1];
    int i,j;
    for(j=0;j<=n;j++)
    {
    	if(j%coins[0]==0)
    	{
    		total[0][j]=1;
    	}
    }
    for(i=1;i<8;i++)
    {
    	for(j=0;j<=n;j++)
    	{
    		if(j>=coins[i])
    		{
    			total[i][j]=total[i-1][j]+total[i][j-coins[i]];
    		}
    		else
    		{
    			total[i][j]=total[i-1][j];
    		}
    	}
    }
    cout<<total[7][n];
    return 0; 
}
