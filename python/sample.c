#include<stdio.h>
#define N=5
void main()
{
   int s[N],N;
   int top=-1;
   void push()
   {
      int x;
      printf("enter the data:");
      scanf("%d",&x);
      if(top>N-1)
      {
	 printf("stavk is overflow");
      }
      else
      {
	 top=top-1;
	 s[top]=x;
      }
   }
   void pop()
   {
      int item;
      if(top==-1)
      {
	 printf("stack is over flow");
      }
      else
      {
	 item=s[top];
	 top=top-1;
	 printf("poped element %d",item);
      }
   }
   void display()
   {
      int i;
      for(i=top,i>=0,i++)
      {
      printf("elements are %d",s[i]);
      }
   }
   void main()
   {
      push();
      push();
      push();
      pop();
      display()
}
