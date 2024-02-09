## Trees are Data Structures defined as follows

- connected
- no cycles
- many children allowed, only one parent
- one root

## Binary Search Trees

- Nodes have one data element and at most two pointers, to `left` and `right` subtrees.
- To get the minimum, look at the leftmost element without a left child.
- To get the maximum, look at the rightmost element without a right child.

## An implementation of BST [[Classes]]

```cpp
class BstNode {
  protected:
    int key ; // or value
    BstNode* left ;
    BstNode* right ;
	public:
		BstNode():left(NULL),right(NULL) { }
		BstNode( int k ):key(k),left(NULL), right(NULL) {} virtual ~BstNode() { delete left ; delete right ; } int getKey() { return key ; }
		BstNode* getLeft() { return left ; }
		BstNode* getRight() { return right ; }
		void setLeft( BstNode* l ) { left = l ; }
		void setRight( BstNode* r ) { right = r ; }
		void printValue() { cout << value ; }
		void bstInsert( int key ) ;
		void bstPrintInorder() ;
		bool bstKeyExists( int key, BstNode*& np ) ;
		int bstMinimum( BstNode*& np ) ;
};
```

### `bstKeyExists(int k, BstNode*& p)` is a recursive member function of this class that returns true if there is a key with the value k in the tree, which p is the root of.

```cpp
bool BstNode::bstKeyExists( int k, BstNode*& p ) { 
	if( key == k ) { p = this ; return true ; } 
	if(k<key){ //must be in left subtree
		if( left == NULL { p=NULL ; return false ; } // Not here.
		return left->bstKeyExists( k, p ) ; // recursive call
	} else { // k>key -> must be in right subtree
		if( right == NULL ) { p = NULL ; return false ; } // Not here.
		return right->bstKeyExists( k, p ); // recursive call
	}
};
```

### `bstMinimum()` employs the strategy of traversing the tree leftwise until we cannot anymore. Note that `bstMaximum()` employs a similar strategy.

```cpp
int BstNode::bstMinimum( BstNode*& p ) {
	if( left == NULL ) { // we are at minimum
		p = this ;
	  return key ;
	} else {
		return left->bstMinimum( p ) ; // recursive call
	}
};
```

### `bstPrintInOrder()` prints the entire left subtree recursively (bottom-up), followed by the right.

```cpp
void BstNode::bstPrintInorder() {
	if( left != NULL ) left->bstPrintInorder() ; // recursive call
	cout << key << " " ;	
	if( right != NULL ) right->bstPrintInorder() ; // recursive call
}
```

### `bstInsert()` will insert a new node with key value k where it should lie in some existing binary search tree.

```cpp
void BstNode::bstInsert( int k ) {

	if( key == k ) return ; // already in tree

	if( k < key ) { // insert in left subtree
		if( left == NULL ){
			left = new BstNode( k );
	  } else {
			left->bstInsert( k );
		}
	} else { // insert in right subtree if( right == NULL )
		if( right == NULL ){
			right = new BstNode( k );
		} else {
			right->bstInsert( k );
		}
	} 
}
```

### `bstDelete()` employs different strategies depending on the number of subtrees the targeted node possesses:

- 0 subtrees
    - delete node, update parent accordingly.
- 1 subtree
    - Parent points to the given subtree, and node is deleted
- 2 subtrees
    - Replace the node key with minimum key of right subtree
    - Delete node with that minimum key

```cpp
void BSTNode::bstDelete( int k, BstNode*& pp) {
	// Choose wether to traverse left or right
	if( k < key ) { // delete from left subtree
		if( left != NULL ) left->bstDelete( k, left ) ;
		return ; 
	}
	if( k > key ) { // delete from right subtree
		if( right != NULL ) right->bstDelete( k, right ) ; 
		return ;
	}
	// we are deleting this node
	if( left==NULL && right==NULL ) { // no children (0)
		pp = NULL ; // set the parent pointer to null.
		delete this ;
	} else if( left==NULL && right!=NULL ) { // only right s.t. (1)
	  pp = right ;
	  right = NULL ;
	  delete this ;
	} else if( left!=NULL && right==NULL ) { // only left s.t. (1)
		pp = left ;
		left = NULL ;
	  delete this ;
	} else { // both (2)
		int minkey = right->bstMinimum() ;
		right->bstDelete( minkey, right ) ; 
	}
}
```

## Implementation of Binary Search Tree [[Classes]]

- We will most often just call the corresponding functions from the `BstNode` class.

```cpp
class BSTree {
  protected:
    BstNode* root;
  public:
		BSTree():root(NULL) {}
		virtual ~BSTree() { delete root ; } 
		BstNode* getRoot() { return root ; } 
		void setRoot( BstNode* p ) { root = p ; }

		void insert( int k ) {
			if( root == NULL ) root = new BstNode( k ) ; 
			else root->bstInsert( k ) ;
			return ;
		}
		void printInorder() {
			if( root != NULL ) root->bstPrintInorder() ; 
			cout << endl ;
			return ;
		}
		bool keyExists( int k, BstNode*& np ) {
			if( root == NULL ) { 
				np = NULL ; 
				return false ; 
			}
			return root->bstKeyExists( k, np ) ; 
		}
		int bstMinimum( BstNode*& np ) { 
			if(root==NULL){
				np=NULL; return-1
			} 
			return root->bstMinimum( np ) ;
		} 
};
```

```C++
/* Definition of the tree node */
class TreeNode {
	public:
		int data;
		TreeNode* left;
		TreeNode* right;
};

/* Recursive helper */
bool is_symmetric_helper(TreeNode* left, TreeNode* right){
	
	if(left==nullptr && right==nullptr){return true;}
	if(left==nullptr || right==nullptr){return false;}
	if(left->data == right->data){
		return is_symmetric_helper(left->left, right->right) && is_symmetric_helper(left->right, right->left);
	}
	return false;
	
}

bool is_symmetric(TreeNode* root) {
	if (root == NULL) {
		return true;
	}
	return is_symmetric_helper(root->left, root->right);
}
```