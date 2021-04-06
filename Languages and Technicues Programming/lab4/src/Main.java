public class Main {

    public static void main(String[] args) {
        int[] a = {1, 1, 2, 3, 0, 1, 1, 2, 3, 0, 5, 8, 13, 21};
        //         0         3    5        8     10        13
        int[] b = {0, 1, 1, 0, 1, 1, 2, 1, 1};
        int[] c = {1, 1, 1, 1, 1, 3, 5};
        Seq s = new Seq(a);
        Seq s2 = new Seq(b);
        Seq s3 = new Seq(c);




        for (int x : s) {
            System.out.println("[" + (x) + ":" + (x+s.maxlen-1) + "]");
        }
        s.set(5, 13);
        for (int x : s) {
            System.out.println("[" + x + ":" + (x+ s.maxlen-1) + "]");
        }

        System.out.println();

        for (int x : s2) {
            System.out.println("[" + x + ":" + (x + s2.maxlen - 1) + "]");
        }

        System.out.println();

        for (int x : s3) {
            System.out.println("[" + (x) + ":" + (x+s3.maxlen-1) + "]");
        }
    }
}
