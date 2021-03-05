public class RingBuffer {
    public final int cap;
    private int head, tail, count;
    private int[] data;


    public RingBuffer() {
        cap = 10;
        head = tail = count = 0;
        data = new int[10];
    }


    public RingBuffer(int n) {
        cap = n;
        head = tail = count = 0;
        data = new int[n];
    }


    public RingBuffer(int[] a) {
        cap = a.length;
        count = a.length;
        head = tail = 0;
        data = new int[cap];
        System.arraycopy(data, 0, a, 0, a.length);

    }


    public void enqueue(int x) {
        if (cap == count) {
            System.out.println("buffer is full");
            return;
        }

        data[tail] = x;
        tail++;
        if (tail == cap)
            tail = 0;
        count++;
    }


    public int dequeue() {
        if (count == 0) {
            System.out.println("buffer is empty");
            return 0; //  ???
        }

        int x = data[head];
        head++;
        if (head == cap)
            head = 0;
        count--;

        return x;
    }


    public boolean empty() {
        if (count == 0)
            return true;
        return false;
    }


    public void print() {
        System.out.print(head + "  " + tail + " - " + count + "\n");
    }

}
