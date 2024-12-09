#include <iostream>
#include <random>
#include <algorithm>
#include <ctime>

class treapNode { // classe per gestire il treap
    public:
        char value;
        int priority;
        treapNode* left;
        treapNode* right;
        treapNode(char v, int p, treapNode* l, treapNode* r);
        friend treapNode* treapInsert(treapNode* root, char val);  
        friend treapNode* rotateLeft(treapNode* root);
        friend treapNode* rotateRight(treapNode* root);
};

treapNode::treapNode(char v, int p, treapNode* l=NULL, treapNode* r=NULL) { // costruttore
    this->value = v;
    this->priority = p;
    this->left = l;
    this->right = r;
}

treapNode* treapInsert(treapNode* root, char val) { // funzione di inserimento

    if (root == NULL) { 
        int prio = rand()%100;; // genera la priorità
        return new treapNode(val, prio); // inserisci il nodo
    }

    if(val > root->value) { // cerca il punto nell'albero in cui inserire il nuovo nodo

        root->right = treapInsert(root->right, val);
        if (root->right && root->right->priority > root->priority) { // se la condizione di priorità non è rispettata
            root = rotateLeft(root); // effettua rotazione per ristabilire 
        }

    }
    if(val < root->value) { 

        root->left = treapInsert(root->left, val); 
         if (root->left && root->left->priority > root->priority) { // se la condizione di priorità non è rispettata
            root = rotateRight(root); // effettua rotazione per ristabilire 
        }

    }

    return root;

}

treapNode* rotateLeft(treapNode* root) {
    treapNode* newRoot = root->right; 
    root->right = newRoot->left;      
    newRoot->left = root;     
    return newRoot;
}

treapNode* rotateRight(treapNode* root) {
    treapNode* newRoot = root->left; 
    root->left = newRoot->right;    
    newRoot->right = root;     
    return newRoot;
}

int main() {
    std::srand(std::time(0));

    std::vector<char> letters;
    for (char ch = 'A'; ch <= 'Z'; ++ch) letters.push_back(ch);
    std::random_shuffle(letters.begin(), letters.end());

    treapNode* root = nullptr;
    
    for(int i = 0; i < 10; i++) { treapInsert(root, letters[i]); }

    return 0;

}

