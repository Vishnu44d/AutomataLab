#include <stdio.h> 
#include <string.h> 
#include <stdlib.h> 
#include <assert.h>

#define true 1
#define false 0
#define MAX 1024

typedef struct dict{
    char *key;
    char *value;
}dict;



void print_tokens(dict token[], int n)
{
	int i;
	printf("Token in the program are: ");
	for(i=0;i<n;++i)
	{
		printf("%s %s", token[i].key,token[i].value);
	}
}

 
char* getSubstring(char* str, int first, int forward) 
{ 
	int i; 
	char* subStr = (char*)malloc(sizeof(char) * (forward - first + 2)); 
	for (i = first; i <= forward; i++) 
		subStr[i - first] = str[i]; 
	subStr[forward - first + 1] = '\0'; 
	return (subStr); 
} 

int isterminal(char s)
{
	if(s==' '||s==';')
		return true;
	return false;
}
 
void getToken(char* str) 
{ 
	int first = 0, forward = 0; 
	int len = strlen(str); 
	dict token[MAX];
	int i = 0;
	
	while (forward <= len && first <= forward) 
	{ 
		if (isterminal(str[forward]) == false) 
			forward++; 

		if (isterminal(str[forward]) == true && first == forward) 
		{ 
			forward++; 
			first = forward; 
		} 
		else if (isterminal(str[forward]) == true && first != forward || (forward == len && first != forward)) 
		{ 
			char* subStr = getSubstring(str, first, forward - 1); 
			printf("%s \n", subStr);
			//strcpy(token[i].key,"Token");
			//strcpy(token[i].value,subStr);
			first = forward; 
			i++;
		} 
	}
	//print_tokens(token, MAX); 
	return; 
} 



int main(void) 
{
	char str[MAX];
    FILE *fptr;
    fptr = fopen("program.c", "r");
    assert(fptr != NULL);
	printf("Tokens are: \n");
    while (fgets(str, sizeof(str), fptr) != NULL) 
    {
            //fprintf(stderr, "%s", str);
            getToken(str);
     }
        
    fclose(fptr);
	return (0); 
} 
