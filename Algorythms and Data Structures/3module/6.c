#include <stdlib.h>
#include <stdio.h>



typedef struct {
      int *heap;
      int cap;
      int count;
} queue;

int max(int a, int b){
      return (a>b) ? a : b;
}


void Swap(int *arr ,int a, int b){
      int t = arr[a];
      arr[a] = arr[b];
      arr[b] = t;
}


void InitPriorityQueque(queue *q, int n){
      q->heap = (int*)malloc(n * sizeof(int));
      q->cap = n;
      q->count = 0;
}


void Insert (queue *q, int element) {
      int i = q->count++;
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
      int time;

      int n;
      scanf("%d\n", &n); // - количество ядер
      queue q;
      InitPriorityQueque(&q, n);
      for(int i = 0; i < n; i++)
            Insert(&q, 0);

      scanf("%d\n", &n); // - количество задач
      int t1, t2;
      for (int i = 0; i < n; i++) {
            scanf("%d %d\n", &t1, &t2);
            time = max(t1, ExtractMax(&q));
            Insert(&q, time+t2);
      }
      heapify(0, q.count, q.heap);

      int max = 0;
      for(int i = 0; i < q.count; i++)
            if(q.heap[i] > max)
                  max = q.heap[i];
      printf("%d\n", max);

      free(q.heap);
      return 0;
}
