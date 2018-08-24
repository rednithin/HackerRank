// https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

#include<iostream>

using namespace std;

int main()
{
  int n, d;
  cin >> n >> d;
  int arr[n];
  for(int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  int freq[201] = {0};
  int summ[201] = {0};
  for(int i = 0; i < d; i++) {
    freq[arr[i]] ++;
  }
  summ[0] = freq[0];
  for(int i = 0; i < 200; i++) {
    summ[i+1] = summ[i] + freq[i+1];
  }
  if(d % 2 == 1) {
    int sum = 0;
    for(int i = d; i < n; i++) {
      int value = arr[i];
      int median = 0;
      int j = 0;
      while (d/2 >= summ[j]) {
        median = j+1;
        j++;
      }
      for(int k = arr[i-d]; k < 201; k++) {
        summ[k] = summ[k] - 1;
      }
      for(int k = arr[i]; k < 201; k++) {
        summ[k] = summ[k] + 1;
      }
      if(value >= 2 * median) {
        sum += 1;
      }
    }
    cout << sum;
  } else {
    int sum = 0;
    for(int i = d; i < n; i++) {
      int value = arr[i];
      int median1 = 0;
      int median2 = 0;
      int j = 0;
      while (d/2 > summ[j]) {
        median1 = j+1;
        j++;
      }
      j = 0;
      while (d/2 + 1 > summ[j]) {
        median2 = j+1;
        j++;
      }
      // cout << value << " " << median1 << " " << median2 << endl;
      for(int k = arr[i-d]; k < 201; k++) {
        summ[k] = summ[k] - 1;
      }
      for(int k = arr[i]; k < 201; k++) {
        summ[k] = summ[k] + 1;
      }
      if(value >= median1 + median2) {
        sum += 1;
      }
    }
    cout << sum;
  }
}