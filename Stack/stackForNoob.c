#include "stdio.h"
//Fixed size stack

//create stack size 


typedef struct Stack{
  int top;
  unsigned capacity;
  int* array;
}stack;


void isStackEmpty(Stack aStack ){
  if (aStack.top == NULL){
    printf("Stack is empty\n");
  }
}


int main(void){

}
