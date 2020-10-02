#include<iostream>
using namespace std;
int main()
{
	int num,numcpy=0,j=0;
	cout<<"Enter the number : ";
	cin>>num;
	int factor[1000];
	for(int i=0;i<num;i++)
	{
		if(num%i==0)
		{
			factor[j]=i;
			j++;
		}
	}
	cout<<endl<<j;
	for(int i=0;i<=j;i++)
	numcpy=numcpy+factor[i];
	if(numcpy==num)
	cout<<"\nNumber is perfect number.";
	else
	cout<<"\nNumber is not perfect number.";
	return 0;
}
