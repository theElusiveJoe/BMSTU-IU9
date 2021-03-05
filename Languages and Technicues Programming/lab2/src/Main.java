public class Main {

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5, 6, 7};
        RingBuffer b1 = new RingBuffer();
        RingBuffer b2 = new RingBuffer(7);
        RingBuffer b3 = new RingBuffer(a);

        System.out.println("переполняем b1:");
        for (int i = 0; i < b1.cap + 1; i++) {
            b1.enqueue(i);
        }
        b1.print();
        System.out.println("почти опустошаем b1");
        for (int i = 0; i < b1.cap - 2; i++) {
            b1.dequeue();
        }
        b1.print();

        System.out.println();
        System.out.println("заполняем b2:");
        for (int i = 0; i < b2.cap; i++) {
            b2.enqueue(i);
        }
        b2.print();
        System.out.println("почти опустошаем b2:");
        for (int i = 0; i < b2.cap-3; i++) {
            b2.dequeue();
        }
        b2.print();

        System.out.println();
        System.out.println("b3 создается уже полным, дозаполнить его нельзя:");
        b3.print();
        b3.enqueue(1);
        System.out.println("переопустошаем b3:");
        for (int i = 0; i < b3.cap + 1; i++) {
            b3.dequeue();
        }
    }
}
