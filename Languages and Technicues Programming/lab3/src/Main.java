import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Segment[] a = new Segment[]{
                new Segment(1, 2, 3, 4),
                new Segment(0, 0, 10, 10),
                new Segment(1, 2, 2, 1),
                new Segment(0, 0, 50, 0),
                new Segment(0, 0, 0, 100)
        };
        Arrays.sort(a);
        for (Segment s : a) System.out.println(s);
    }


}
