#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct Node{
	int k;
	char v[10];
      struct Node *parent;
      struct Node *left;
      struct Node *right;
      int count;
} node;


node* init(){
	node *y = (node*)malloc(sizeof(node));
      y->parent = NULL;
      y->left = NULL;
      y->right = NULL;
      y->count = 0;

	return y;
}


typedef struct {
	node *root;
} tree;


void insert(tree *t, int k, char* v){
	node *y = init();
      y->k = k;
      strcpy(y->v, v);

	if (t->root == NULL){
		t->root = y;
	}else{
      	node *x = t->root;
      	while (1){
      		x->count++;
      		if (k < x->k){
      			if (x->left == NULL){
      				x->left = y;
      				y->parent = x;
                              if(y->left!=NULL)
                                    y->count +=y->left->count+1;
                              else
                                    y->count = 0;
      				break;
      			}
      				x = x->left;
      		} else {
      			if (x->right == NULL){
      				x->right = y;
      				y->parent = x;
                              if(y->left!=NULL)
                                    y->count +=y->left->count+1;
                              else
                                    y->count = 0;
      				break;
                        }
      			x = x->right;
      		}
      	}
      }
}


node* findIndex(tree *t, int k){
      node *x = t->root;
      int cur = 0;
      if (x->left != NULL){
            cur += x->left->count + 1;
      }
      while(1){
            if (cur == k){
                  return x;
            } else if (cur < k) {
                  x = x->right;
                  cur++;
                  if (x->left != NULL){
                        cur += x->left->count+1;
                  }
            } else {
                  x = x->left;
                  cur--;
                  if (x->right != NULL){
                        cur -= x->right->count+1;
                  }
            }
      }
      return x;
}


char* search(tree *t, int k){
	node *y = findIndex(t, k);
	return y->v;
}


node* descend(tree* t, int k){
      node *x = t->root;

	while (x!=NULL && (x->k != k)){
		if (x->k > k)
			x = x->left;
		else
			x = x->right;
	}
	return x;
}


char* lookup(tree *t, int k){
	node *y = descend(t, k);
	return y->v;
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


void delete(tree *t, int k){
	node *x = descend(t, k);

      if(x->left == NULL && x->right == NULL){
            if(x->parent!=NULL){
                  node *p = x;
                  while(p->parent!= NULL){
                        p = p->parent;
                        p->count--;
                  }
            }
            replace(t, x, NULL);
      } else if(x->left == NULL){
            if(x->parent!=NULL){
                  node *p = x;
                  while(p->parent!= NULL){
                        p = p->parent;
                        p->count--;
                  }
            }
            replace(t, x, x->right);
      } else if(x->right == NULL){
            if(x->parent!=NULL){
                  node *p = x;
                  while(p->parent!= NULL){
                        p = p->parent;
                        p->count--;
                  }
            }
            replace(t, x, x->left);
      } else {
            node *y = succ(x);
            if(y->parent!=NULL){
                  node *p = y;
                  while(p->parent!= NULL){
                        p = p->parent;
                        p->count--;
                  }
            }
		replace(t, y, y->right);
		x->left->parent = y;
		y->left = x->left;

		if (x->right)
			x->right->parent = y;

		y->right = x->right;
		y->count = x->count;
		replace(t, x, y);
      }

	free(x);
}





void freeTree(node *x){
      if (x->left != NULL)
            freeTree(x->left);
      if (x->right != NULL)
            freeTree(x->right);
      free(x);
}


void printtree(node *root){
      if (root != NULL){
            printf("   %d(%d)\n", root->k, root->count);

            if (root->left != NULL)
                  printf("%d     ", root->left->k);
            else
                  printf("null   ");

            if (root->right != NULL)
                  printf("%d     \n\n", root->right->k);
            else
                  printf("null   \n\n");
      }


      if (root->left != NULL)
            printtree(root->left);
      if (root->right != NULL)
            printtree(root->right);
}



int main(){
	int n = 0;
	scanf("%d", &n);

	tree *t = (tree*)malloc(sizeof(tree));
	t->root = NULL;

      char v[10];

	char cmd[10];
	int k;
	for (int i = 0; i < n; i++){
		scanf("%s\n", cmd);
            scanf("%d\n", &k);

		if (!strcmp(cmd, "INSERT")){
			scanf("%s", v);
			insert(t, k, v);
            } else if (!strcmp(cmd, "SEARCH")) {
                  printf("searching %d :  ", k);
                  printf(" ");
                  printf("%s \n", search(t, k));
            } else if (!strcmp(cmd, "LOOKUP")) {
                  printf("looking %d :  ", k);
                  printf("%s\n", lookup(t, k));
		} else {
                  delete(t, k);
            }
            //printf("************\n");
            //printtree(t->root);
            //printf("************\n");
	}

	freeTree(t->root);
	free(t);

	return 0;
}
