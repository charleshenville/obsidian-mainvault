## Benefit and Motivation

- O(1) average performance on search/insert/delete.
- Using a 2D array, `table` that is at least 1.3 times as large as max. element capacity of it.
- Using [[Hash Functions]], h(k) that map each key, k to a specific array index.

## Reducing Collision Probability

- Making avg. length of lists 1 → O(1)
- We can make out hash table larger.
- We can use better [[Hash Functions]].
    - Making table size a prime number.
    - Good hash functions usually involve multiplication by a large prime: `h(k)=(k*p)%m`

## Open Hashing

```cpp
class Node{
	public:
		int key;
		Node* next;
		~Node(){delete next;}
};
class List{
	private:
		Node * head;
	public:
		List(); // sets head to null
		bool isEmpty(); // returns true if head is NULL
		void insert(int v); // insertion at head
		Node* remove(int k); // remove node with key==k
		bool isFound(int k); // return true if node in list with key==k
		~List();
}
```

![[Untitled (4).png]]

```cpp
#define SIZE 7

class HashTable{
	private:
		List** table;
	public:
		HashTable(){
			table = new List*[SIZE];
			for(int i=0; i<SIZE; i++){
				table[i]=NULL;
			}
		}
		bool search(int v){
			int idx= v%SIZE;
			if(table[idx] != null){
				return table[idx]->isFound(v);
			}else{
				return false;
			}
		}
		void insert(int v){
			if(search(v)){ // if it already exists, do nothing.
				return;
			}else{
				int idx = v % SIZE;
				if(table[idx] == NULL){
					table[idx] = new List;
				}
				table[idx]->insert(v);
			}
		}
		~HashTable(){
			for(int i=0; i<SIZE; i++){
				delete table[i];
			}
			delete [] table;
		}
		void remove(int v){
			if(!search(v)){
				return;
			}else{
				int idx = v % SIZE;
				table[idx]->remove(v);
			}
		}
}
```

## Linear Probing

- Brute force your way to find the first index where there is no collision.
    - Collision at `h(k)`? Try `(h(k)+1) % m`.
    - Collision again? Try `(h(k)+2) % m`.
    - And so on.

## Quadratic Probing

- if collision at `h(k)`, then probe `(h(k)+12)%m`
- if collision there, probe `(h(k)+22)%m`
- if collision there, probe `(h(k)+32)%m`
- And so on.

## Double Hashing

- if collision at `h(k)`, then probe `(h(k)+h2(k))%m`
- if collision there, probe `(h(k)+2h2(k))%m`
- if collision there, probe `(h(k)+3h2(k))%m`
- And so on.

![[Untitled (5).png]]

## An example hash table implementation in C++:
```C++
#include <iostream>
#define INIT_CAPACITY 32
using namespace std;

class ListNode {
	public:
		ListNode(const string& name_) {
			name = name_;
			next = NULL;
		};
		string name;
		ListNode* next;
};
class LinkedList {
	private:
		ListNode* head;
	
	public:
		// Default constructor: initialize the head to NULL.
		LinkedList();
		
		// Return true if and only if the list is empty,
		bool is_empty();
		
		// Insert the given node to the head of the list.
		// Time complexity: 0(1)
		void insert(ListNode* node);
		
		// Traversing from the head. Remove the first node found with the given
		// name from the list. The removed node is NOT deallocated.
		// Returns this node (or NULL if the name is not found).
		// Time complexity: 0(n)
		ListNode* remove(const string& name);
		
		// Return true if there exists at least one node with the given name.
		// Time complexity: 0(n)
		bool find(const string& name);
		
		// Remove the current head node from the linked list,
		// and return it.
		// Move the head one node forward.
		// Time complexity: 0(1)
		ListNode* pop_head();
		
		// Destructor: Properly deallocate all the nodes.
		~LinkedList();
};

class HashTable {
	private:
		// Array of Linked List: resolving collisions by chaining
		LinkedList** table;
		// The length of the table array,
		int table_slot_size;
		// Keep track of how many elements (names) are in the hash table
		int num_elements;
		int get_hash_index(const string& name) {
			return string_hash(name) % table_slot_size;
		}

	public:
		// Constructors and destructors.
		~HashTable(){
			for(int i=0; i<table_slot_size; i++){
				delete table[i];
			}
			delete [] table;
		}
		HashTable() {
			table = new LinkedList*[INIT_CAPACITY];
			table_slot_size = INIT_CAPACITY;
			num_elements = 0;
			for (int i = 0; i < table_slot_size; ++i) {
				table[i] = NULL;
			}
		}
		// Hash table method,
		bool exist(const string& name) {
			int idx = this->get_hash_index(name);
			if (table[idx] == NULL) {
				return false;
			}
			return table[idx]->find(name);
		}
		bool HashTable::insert(const string& name) {
			if (this->exist(name)) {
				return false;  // found!
			}
			
			// not found!
			if (num_elements + 1 >= table_slot_size) {
				table_slot_size = table_slot_size * 2;
				LinkedList** newTable = new LinkedList*[table_slot_size];
				for (int i = 0; i < table_slot_size; i++) {
					newTable[i] = nullptr;
				}
				
				for (int i = 0; i < table_slot_size / 2; ++i) {
					if (table[i] != NULL) {
						ListNode* n = table[i]->pop_head();
						while (n != NULL) {
							int idx = get_hash_index(n->name);
							if (newTable[idx] == NULL) {
								newTable[idx] = new LinkedList;
							}
							newTable[idx]->insert(n);
							n = table[i]->pop_head();
						}
						delete table[i];
					}
				}
				delete[] table;
				table = newTable;
			}
			
			int idx = this->get_hash_index(name);
			
			if (table[idx] == NULL) {
				table[idx] = new LinkedList;
			}
			ListNode* n = new ListNode(name);
			table[idx]->insert(n);
			num_elements++;
			return true;
		}
		bool remove(const string& name){
			if (!this->exist(name)) {
				return false;
			}
			int idx = this->get_hash_index(name);
			table[idx]->remove(name);
			num_elements--;
			return true;
		}
		bool change_name(const string& old_name, const string& new_name){
			if (!this->exist(old_name)||this->exist(new_name)) {
				return false;
			}
			int idx = this->get_hash_index(old_name);
			table[idx]->remove(old_name);
			idx = this->get_hash_index(new_name);
			if (table[idx] == NULL) {
				table[idx] = new LinkedList;
			}
			table[idx]->insert(new_name);
			return true;
		}
};
```