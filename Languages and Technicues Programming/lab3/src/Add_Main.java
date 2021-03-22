import java.util.Arrays;

public class Add_Main {

    public static void main(String[] args) {

        Point[] a = new Point[]{
                new Point(1, 0, 0),
                new Point(0, 1, 0),
                new Point(0, 0, 1),
        };
        Point[] b = new Point[]{
                new Point(13, 12, 34),
                new Point(-10, -2, -80),
                new Point(10, 11, -40),
        };
        Point[] c = new Point[]{
                new Point(100, 200, 300),
                new Point(100, 200, 300),
                new Point(100, 200, 300),
                new Point(-10, -2, -80),
                new Point(10, 11, -40),
        };

        Points[] s = new Points[]{new Points(a, "a"), new Points(b, "b"), new Points(c, "c")};

        Arrays.sort(s);
        for (Points si : s) System.out.println(si);
    }
}