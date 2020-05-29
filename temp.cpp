#include <bits/stdc++.h>
using namespace std;

int main()
{	
	#ifndef O_J
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif


	cout << "Helloo ";
	return 0;
	int n;
	cin >> n;
	int arr[n];
	for(int i=0;i<n;i++)cin>>arr[i];

	int cursum,maxsum;
	cursum=arr[0];
	maxsum=arr[0];

	for(int i=1;i<n;i++)
	{
		int temp = cursum + arr[i];
		cursum = max( temp, arr[i]);
		// if( temp < 0 )cursum = arr[i];

		if(cursum > maxsum)maxsum = cursum;

	}

}