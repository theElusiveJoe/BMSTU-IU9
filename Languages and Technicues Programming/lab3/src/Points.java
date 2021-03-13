import java.util.ArrayList;

public class Points implements Comparable<Points> {
    ArrayList<Point> ps;
    String name;

    Points(Point ps[], String s) {
        name = s;
        this.ps = new ArrayList<Point>();
        for (Point p : ps)
        this.ps.add(p);
    }

    public float getLenOfAverageVect() {
        float x = 0, y = 0, z = 0;
        for (Point p : ps) {
            x += p.x;
            y += p.y;
            z += p.z;
        }
        x /= ps.size();
        y /= ps.size();
        z /= ps.size();
        return x * x + y * y + z * z;
    }


    public int compareTo(Points a) {
        if (this.getLenOfAverageVect() > a.getLenOfAverageVect()) {
            return 1;
        } else {
            return -1;
        }
    }

    public String toString(){
        return this.name;
    }
}
