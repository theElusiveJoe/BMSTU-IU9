#include <stdlib.h>
#include <stdio.h>

typedef struct PriorityQueque {
      int *heap;
      int cap;
      int count;
} queue;



void Swap(int *arr ,int a, int b){
      int t = arr[a];
      arr[a] = arr[b];
      arr[b] = t;
}


void Ilenert (queue *q, int element) {
      int i = q->count++;
      printf("%d %d\n",i, q->cap);
      if (i == q->cap) {
            printf("overflow\n");
            return;
      }
      q->heap[i] = element;
      while (i > 0 && q->heap[(i - 1) / 2] > q->heap[i]){
            Swap(q->heap, (i-1)/2, i);
            i = (i - 1)/ 2;
      }

}


void heapify(int i, int nel, int* base){
      int l = 2*i + 1;
      int r = l+1;
      int j = i;

      while(1){
            l = 2*i + 1;
            r = l+1;
            j = i;
            if(l < nel && base[i] > base[l])
                  i = l;
            if(r < nel && base[i] > base[r])
                  i = r;
            if(i == j)
                  break;
            Swap(base, i, j);
      }
}

int ExtractMax (queue *q){
      if (!q->count) {
            printf("void");
            return 0;
      }
      int element = q->heap[0];
      q->count--;
      if (q->count > 0) {
            q->heap[0] = q->heap[q->count];
            heapify(0, q->count, q->heap);
      }
      return element;
}


int main(){
      int n;
      scanf("%d\n", &n);
      int t, len = 0;
      for (int i = 0; i < n; i++) {
            scanf("%d ", &t);
            len += t;
      }

      queue q;
      q.heap = (int*)malloc(len*sizeof(int));
      q.cap = len;
      q.count = 0;

      for (int i = 0; i < len; i++) {
            scanf("%d", &t);
            Ilenert(&q, t);
      }
      while (q.count > 0)
            printf("%d ", ExtractMax(&q));

      free(q.heap);
      return 0;
}
