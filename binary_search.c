#include <stdio.h>

int main()
{
   //declaring variables..
  int i;//for iteration
  int first;//for storing first element
  int last;//for storing last element
  int middle;//for storing middle element
  int n;//storing number of elements
  int search;//used to store search value
  int array[100];

  //taking no.of elements from user
  printf("Enter no. of elements: \t");
  scanf("%d",&n);

  printf("Enter %d integers: \n",n);

  //storing elements in array
  for(i=0; i < n; i++){
    scanf("%d",&array[i]);
  }

  //taking search value from user
  printf("Enter value to be search in array:\n");
  scanf("%d",&search);


  first = 0;//initialize first value to be 0
  last = n-1;//n-1 is done because array index is started from 0 so if n=4 index is 0,1,2,3
  middle = (first + last)/2;//calculate middle element


  while (first <= last)
  {
    if (array[middle] < search)
      first = middle + 1;
    else if (array[middle] == search) 
    {
      printf("%d found at location %d.\n", search, middle+1);
      break;
    }
    else
      last = middle - 1;
      middle = (first + last)/2;
  }
  if (first > last)
    printf("Not found! %d isn't present in the list.\n", search);

  return 0;
}