Purpose:
- Taking a larger problem, Identifying a base case, and splitting it up into smaller, more manageable problems. 

## Infamous and magnificent factorial example:
```cpp
int factorial(int n){
	// Base case:
	if (n==1||n==0){
		return 1;
	}
	// Recursive (Other) Case:
	return n * factorial(n-1);
}
```

## Given an array of n, integers, return the sum of the array's elements:
```cpp
int sumElements(int *arr, int n){
	if (n<1){return 0;}
	return arr[n-1] + sumElements(arr, n-1);
}
```

## Given a [[Linked Lists]] Object, print the nodes recursively:
```cpp
class Node {
	public: 
	int data; 
	Node *head; 
};

void recursivePrint(Node *p){
	if(p==nullptr){return;}
	cout << p->data;
	recursivePrint(p->next);
}

int main(){
	List L;
	//...
	recursivePrint(L->getHead()); // Accomplishes this task.
}
```