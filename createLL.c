
#include <stdio.h>
#include <stdlib.h>

int main() {
  struct Node{
    int data;
    struct Node *next;
  };

  struct Node *head,*newnode,*temp;
  int choice=1;

  head = 0;
  while(choice)
  {
  //creating node
      newnode = (struct Node*)malloc(sizeof(struct Node));

      printf("Enter data:");
      scanf("%d",&newnode->data);//assign data in newly created node
      newnode->next =0;//assign null in newly node next part

      if(head == 0){
        head = temp = newnode;
      }
      else
      {
        temp ->next = newnode;//taking temp pointer to store newly created next part to hold address
      }
      printf("do you want to continue?");
      scanf("%d",&choice);
  }


  //printing linked list through loop
  temp = head;//assign head address in temp

  while(temp !=0)
  {
    printf("%d ",temp->data);
    temp = temp->next;//assign next node address in temp

  }
 

}