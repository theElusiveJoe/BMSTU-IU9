public class Segment implements Comparable<Segment> {
    public int x1, y1, x2, y2;

    Segment(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    float foo(int x) {
        float k;
        if (x1 == x2) {
            return x;
        } else k = ((float) (this.y2 - this.y1)) / (this.x1 - this.x2);
        float b = this.y1 - k * this.x1;
        return k * x + b;
    }

    int numberOfPoints() {
        if (x1 == x2) {
            return Math.abs(y2 - y1) + 1;
        } else {
            int count = 0;
            for (int i = this.x1; i <= this.x2; i++) {
                if (foo(i) == Math.round(foo(i))) {
                    count++;
                }
            }
            return count;
        }
    }

    public int compareTo(Segment a) {
        return this.numberOfPoints() - a.numberOfPoints();
    }

    public String toString() {
        return "(" + x1 + ";" + y1 + ") -- (" + x2 + ";" + y2 + ")";
    }
}
