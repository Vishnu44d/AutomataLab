#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct Stack 
{ 
    int top; 
    unsigned capacity; 
    int* array; 
}; 

struct Stack* createStack( unsigned capacity ) 
{ 
    struct Stack* stack = (struct Stack*) malloc(sizeof(struct Stack)); 
  
    if (!stack)  
        return NULL; 
  
    stack->top = -1; 
    stack->capacity = capacity; 
  
    stack->array = (int*) malloc(stack->capacity * sizeof(int)); 
  
    if (!stack->array) 
        return NULL; 
    return stack; 
} 
int isEmpty(struct Stack* stack) 
{ 
    return stack->top == -1 ; 
} 
char peek(struct Stack* stack) 
{ 
    return stack->array[stack->top]; 
} 
char pop(struct Stack* stack) 
{ 
    if (!isEmpty(stack)) 
        return stack->array[stack->top--] ; 
    return '$'; 
} 
void push(struct Stack* stack, char op) 
{ 
    stack->array[++stack->top] = op; 
} 
  

int isOperand(char ch) 
{ 
    return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'); 
} 
  
int Prec(char ch) 
{ 
    switch (ch) 
    { 
    case '|': 
        return 1; 
  
    case '.': 
        return 2; 
  
    case '*': 
        return 3; 
    } 
    return -1; 
} 
  

int infixToPostfix(char* exp) 
{ 
    int i, k; 
  
    struct Stack* stack = createStack(strlen(exp)); 
    if(!stack)  
        return -1 ; 
  
    for (i = 0, k = -1; exp[i]; ++i) 
    { 
        if (isOperand(exp[i])) 
            exp[++k] = exp[i]; 
          
        else if (exp[i] == '(') 
            push(stack, exp[i]); 

        else if (exp[i] == ')') 
        { 
            while (!isEmpty(stack) && peek(stack) != '(') 
                exp[++k] = pop(stack); 
            if (!isEmpty(stack) && peek(stack) != '(') 
                return -1;             
            else
                pop(stack); 
        } 
        else 
        { 
            while (!isEmpty(stack) && Prec(exp[i]) <= Prec(peek(stack))) 
                exp[++k] = pop(stack); 
            push(stack, exp[i]); 
        } 
  
    } 
  
    while (!isEmpty(stack)) 
        exp[++k] = pop(stack ); 
  
    exp[++k] = '\0'; 
    printf( "%sn", exp ); 
} 

int retIndex(char *alphabet,char c)
{
    int i;
    for(i=0;i<strlen(alphabet);i++)
    {
        if(c==alphabet[i])
            return i-1;
    }
    return -1;
}

int isAccepted(int finals[],int z,int f)
{
    int i=0;
    for(i=0;i<z;i++)
    {
        if(f==finals[i])
            return 1;
    }
    return 0;
}


void dfa()
{
    int s,i,j,k,y,z;
    printf("number of states:\n");
    scanf("%d",&s);
    printf("number of inputs:\n");
    scanf("%d",&i);
    int d[20][20];
    printf("Enter the transition function:\n");
    for(j=0;j<s;j++)
    {
        for(k=0;k<i;k++)
        {
    
            scanf("%d",&d[j][k]);
        }
    }
    printf("initial state:\n");
    scanf("%d",&y);
    y=y-1;
    printf("number of final states:\n");
    scanf("%d",&z);
    int finals[20];
    printf("final states:\n");
    for(j=0;j<z;j++)
    {
        scanf("%d",&finals[j]);
    }
    char alphabet[20], str[400];
    printf("enter the alphabets:\n");
    for(j=0;j<=i;j++)
    {
        alphabet[j]=getchar();
    }
    /*
    for(j=0;j<=i;j++)
    {
        printf("%c",alphabet[j]);
    }*/
    printf("\nenter the string:\n");
    scanf("%s",str);
    /*printf("%s",str);
    printf("%d",retIndex(alphabet,'a'));
    printf("%d",isAccepted(finals,z,1));
    */
    printf("---------------------------\n\n");
    printf("The intermediate steps are:\n\n");
    int p;
    printf("prev state\tcurr char\tnext state\t\n");
    for(j=0;j<strlen(str);j++)
    {
        p=retIndex(alphabet,str[j]);
        printf("%d  \t\t  ", y+1);
        y=d[y][p] - 1;
        printf("%c  \t\t   %d\n",str[j], y+1);
        
    }
    if(isAccepted(finals,z,y+1) == 1)
    {
        printf("---------ACCEPTED------------\n");
    }
    else
    {
        printf("-------NOT ACCEPTED----------\n");
    }
}



int main(void)
{

    system("python3 re2nfa.py");
    return 0;
}
