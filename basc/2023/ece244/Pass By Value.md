### Implementation of a factorial function:
$$n! = n * (n-1) * (n-2) * … * 1​$$
``` C++
int factorial(int n){
	
	int fact = 1;
	for(int i = 1; i<=n; i++){
		fact *= i;
	}
	n = 0 // Does NOT Change the value of n in main.
	return fact;
    
}

int main(){

	int n = 4;
	int factN = factorial(n); // Pass by value here
	
	cout << "Factorial of" << n << "is" << factN;
	return 0;

}
```
