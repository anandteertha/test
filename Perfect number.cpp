#include<iostream>
using namespace std;
int main()
{
	int num,numcpy=0,j=0;
	cout<<"Enter the number : ";
	cin>>num;
	int factor[num];
	for(int i=1;i<=num-1;i++)
	{
		if(num%i==0)
		{
			factor[j]=i;
			j++;
		}
	}
	for(int o=0;o<j;o++)
	{
		numcpy=numcpy+factor[o];
	}
	if(numcpy==num)
	{
		cout<<"\nNumber is perfect number.";
	}
	else
	{
		cout<<"\nNumber is not perfect number.";
	}
	return 0;
}
