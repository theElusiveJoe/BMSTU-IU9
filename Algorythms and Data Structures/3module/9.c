#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct Node{
	int k;
	int v;
      int balance;
      struct Node *parent;
      struct Node *left;
      struct Node *right;
} node;


typedef struct {
	node *root;
} tree;

node* init(){
	node *y = (node*)malloc(sizeof(node));
      y->parent = NULL;
      y->left = NULL;
      y->right = NULL;
	return y;
}


node* insert(tree *t, int k, int v){
	node *y = init();
      y->k = k;
      y->v = v;

	if (t->root == NULL){
		t->root = y;
	} else {
      	node *x = t->root;
      	while (1){
      		if (k < x->k){
      			if (x->left == NULL){
      				x->left = y;
      				y->parent = x;
      				break;
      			}
      				x = x->left;
      		} else {
      			if (x->right == NULL){
      				x->right = y;
                              y->parent = x;
      				break;
                        }
      			x = x->right;
      		}
      	}
      }

      return y;
}


void replace(tree *t, node *x, node *y){
	if (x == t->root){
		t->root = y;
		y->parent = NULL;
	} else {
      	node *p = x->parent;
      	if (y != NULL)
      		y->parent = p;

      	if (p->left == x)
      		p->left = y;
      	else
      		p->right = y;
      }
}


void rotateLeft(tree *t, node *x){
      node *y = x->right;
      replace(t, x, y);
      node *b = y->left;
      if (b != NULL)
            b->parent = x;
      x->right = b;
      x->parent = y;
      y->left = x;

      x->balance--;
      if (y->balance > 0)
            x->balance -= y->balance;
      y->balance--;
      if (x->balance < 0)
            y->balance += x->balance;
}

void rotateRight(tree *t, node *x){
      node *y = x->left;
      replace(t, x, y);
      node *b = y->right;
      if (b != NULL)
            b->parent = x;
      x->left = b;
      x->parent = y;
      y->right = x;

      x->balance--;
      if (y->balance > 0)
            x->balance -= y->balance;
      y->balance--;
      if (x->balance < 0)
            y->balance += x->balance;
}


void insertAVL(tree *t, int k, int v){
      node *a = insert(t, k, v);
      a->balance = 0;
      while(1){
            node *x = a->parent;
            if (x == NULL)
                  break;
            if (a==x->left){
                  x->balance--;
                  if(x->balance == 0)
                        break;
                  if(x->balance == -2){
                        if (a->balance == 1)
                              rotateLeft(t, a);
                        rotateRight(t, x);
                        break;
                  }
            } else {
                  x->balance++;
                  if(x->balance == 0)
                        break;
                  if(x->balance == 2){
                        if (a->balance == -1)
                              rotateRight(t, a);
                        rotateLeft(t, x);
                        break;
                  }
            }
            a = x;
      }
}


node* minimum(node *t){
	node *x;
	if (t == NULL){
		return NULL;
	} else {
		x = t;
		while (x->left != NULL)
			x = x->left;
	}

	return x;
}


node* succ(node *x){

	if (x->right){
		return minimum(x->right);
	} else {
            node *y = x;
		y = x->parent;

		while (y != NULL && x == y->right){
			x = y;
			y = y->parent;
		}
            return y;
	}
}


void freeTree(node *x){
      if (x->left != NULL)
            freeTree(x->left);
      if (x->right != NULL)
            freeTree(x->right);
      free(x);
}




void printtree2(node *root){
      if (root != NULL){
            printf("  %d   \n", root->k);

            if (root->left != NULL)
                  printf("%d   ", root->left->k);
            else
                  printf("null   ");

            if (root->right != NULL)
                  printf("%d\n\n", root->right->k);
            else
                  printf("null   \n\n");
      }


      if (root->left != NULL)
            printtree2(root->left);
      if (root->right != NULL)
            printtree2(root->right);
}


int createHash(char *name){
      int h = 0;
      int p = 1;
      int letter;
      for(int i = 0; i < strlen(name); i++){
            letter = name[i];
            if (letter <= 57)
                  letter-=48;
            else
                  letter-=66;

            h += letter*p;
            p*=37;
      }
      return h;
}


int lookup(tree* t, int k){
      node *x = t->root;
      if(x == NULL)
            return -1;

	while (x!=NULL && (x->k != k)){
		if (x->k > k){
                  if(x->left == NULL)
                        return -1;
			x = x->left;
            }
		else {
                  if(x->right == NULL)
                        return -1;
			x = x->right;
            }
	}
	return x->v;
}





int main(){
	int n = 0;
	scanf("%d\n", &n);

	tree *t = (tree*)malloc(sizeof(tree));
	t->root = NULL;


      // 0 - еще не известное
      // 1 - CONST
      // 2 - SPEC
      // 3 - IDENT
      int identnum = 0;
	char ch;
      int flag = 1;
      int val;
      char specs[] = "+-*/()";
      char name[30];
      int j, i = 0;

	while(i < n){
            if (flag){
                  scanf("%c", &ch);
                  //printf("scanned: %c, i = %d\n", ch, i);
                  i++;
            }
            flag = 1;

            if(ch >= 40 && ch <= 47){
                  printf("SPEC ");
                  for(j = 0;;j++){
                        if(ch == specs[j]){
                              printf("%d\n", j);
                              break;
                        }
                  }
            }else if(ch >= 48 && ch<=57){
                  val = 0;
                  while (i < n && (ch >= 48 && ch<=57)) {
                        val += ch-48;
                        val*=10;
                        scanf("%c", &ch);
                        //printf("scanned: %c, i = %d\n", ch, i);
                        i++;
                  }
                  val/=10;
                  flag = 0;
                  printf("CONST %d\n", val);
            } else if(ch >= 65 && ch<=122){
                  int k = 0;
                  while (i <= n && ((ch >= 65 && ch<=122) || (ch>=48 && ch<=57))) {
                        name[k] = ch;
                        k++;
                        if(i == n)
                              break;
                        scanf("%c", &ch);
                        //printf("scanned: %c, i = %d\n", ch, i);
                        i++;
                  }
                  name[k] = 0;
                  int h = createHash(name);
                  val = lookup(t, h);
                  if(val == -1){
                        val = identnum;
                        insertAVL(t, h, identnum);
                        identnum++;
                  }
                  flag = 0;
                  printf("IDENT %d\n", val);
            }
      }


	freeTree(t->root);
	free(t);

	return 0;
}
