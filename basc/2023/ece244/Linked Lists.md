## Linked list with [[Classes]] Objects and using [[Destructors]] on them IOT free memory when using [[Pointers]].

```cpp
class ComplexNum{
	public:
		double real;
		double img;
		ComplexNum * next;
		ComplexNum(){
			real = 0;
			img = 0;
			next = nullptr;
		}
		~ComplexNumber(){
			
			if(next!=nullptr){ // must make this condition else we get an error trying to delete something that dne.
				delete next;
			}
		}
};

int main(){
	ComplexNum * px = new ComplexNum; // Dynamically allocates space for a ComplexNum Object
	// Note that the line above also calls the constructor.
	px -> real = 8;
	px -> next = new ComplexNum;
	
	delete px; // When we do this, we recursively delete the whole linked list with out Destructor defn.

}
```

## If we want to Extend an Array:

```cpp
int arr [3] = {1,2,3};
```

|1|2|3|
|---|---|---|

|1|2|3|4|
|---|---|---|---|

We must perform a copy and extension via a new array.

## Linked Lists Solve this:

```mermaid
graph LR
  1 --> 2 --> 3 ---> NULL
```

### 2 Variables for each node:

- `int` for value.
- pointer `*` to a node.

```cpp
class Node {

	private:
		int data;
		Node * next;
	public:
		Node(){data=0; next=NULL;}
		Node(int d){data=d; next=NULL;}
		Node(int d, Node* n){
			data=d;
			next=n;
		}
		~Node(){
			delete next;
		}
		int getData(){return data;}
		Node* getNext(){return next;}
		void setData(int d){data=d;}
		void setNext(Node*n){next=n;}
};
```

```cpp
// Boolean Searching
bool dataExists(int d){

		Node* current = head;
		while(current->getData()!=d){
			if (current->getNext()==NULL || current->getData() > d){
				return false;
			}else{
				current = current->getNext();
			}
		}
		return true;
	}
	// Or 
	bool data Exists (int d) {
		Node* p= head ;
		while(p!= NULL && P->getData()<d)
		{

			if (p-> getData == d) {
				return true;
			}
			else {
				p=p->getNext();
			}
		
		}
	}
```

```cpp
// Inserting data into a sorted linked list:

bool List::insertData(int d){
	Node *n = new Node(d);
	Node *p = head, *prev = NULL;
	
	if(p==NULL){
		head = n;
	}
	while(p!=NULL && p->getData()<d){
		prev = head;
		p = p->getNext;
	}
	n->setNext(p);

	if(prev==NULL){
		head = n;
	}
	else{
		prev->setNext(n);
	}
}
```

```cpp
// Deleting Data from a sorted linked list

bool List::deleteData(int d){

	Node *p=head; *prev=NULL;
	while(p!=NULL && p->getData()!= d){
		if(p->getData() > d) return false;
		prev = p;
		p = p->getNext();
	}
	if(p==NULL) return false;
	// Otherwise p is the node we wish to delete:
	if(prev==NULL){
		head = p->getNext(); // front insert
	}else{
		prev->setNext(p->getNext());
	}
	p->setNext(NULL); // GP
	delete p;
}
```

```cpp
// Deep Copy of Our LL

//Deconstructor
List::~List(){
	delete head;
}
List::List(const List& original){
	Node *p = original.head;
	Node *np = NULL; // NEW Pointer. We will do more allocations.
	
	head = NULL;

	while(p!=NULL){
		Node *n = new Node(p->getData(), NULL);
		if(np==NULL){
			head = n;
		}
		else{
			np->setNext(n);
		}
		p = p -> getNext();
		np = n;
	}
}
```

Operator= 
```C++
List& List::operator=(const List& original){
	
	if (&original == this){
		return *this;
	}
	if (head != NULL){
		delete head;
		head = NULL;
	}

	Node *p = original.head;
	Node *np = NULL; // NEW Pointer. We will do more allocations.
	
	head = NULL;

	while(p!=NULL){
		Node *n = new Node(p->getData(), NULL);
		if(np==NULL){
			head = n;
		}
		else{
			np->setNext(n);
		}
		p = p -> getNext();
		np = n;
	}
	
	return *this;

}
```