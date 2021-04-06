import java.util.Iterator;
import java.util.ArrayList;

public class Seq implements Iterable<Integer> {
    private ArrayList<Integer> seq;
    int maxlen;

    public Seq(int[] A) {
        this.seq = new ArrayList<Integer>();
        for (int i = 0; i < A.length; i++) {
            seq.add(A[i]);
        }
        maxlen = getMaxLen();
    }

    public void add(int x) {
        System.out.println("\n adding" + x);
        seq.add(x);
        maxlen = getMaxLen();
    }

    public void remove(int i) {
        if (i >= seq.size())
            System.out.println("index out of sequence");
        else {
            System.out.println("\n removing seq[" + i + "]");
            seq.remove(i);
            maxlen = getMaxLen();
        }
    }

    public void set(int x, int i) {
        if (i >= seq.size())
            System.out.println("index out of sequence");
        else {
            System.out.println("changing seq[" + i + "] to " + x);
            seq.set(i, x);
            maxlen = getMaxLen();
        }
    }

    public int getMaxLen() {
        int maxcount = 0;
        for (int i = 0; i < seq.size() - maxcount; i++) {
            int f1 = 1, f2 = 1, fd, count = 0;

            if (seq.size() > i + 1 && seq.get(i) == 1 && seq.get(i + 1) == 1) {
                f2 = 0;
            }

            while ((seq.get(i)) > f1) {
                fd = f1 + f2;
                f2 = f1;
                f1 = fd;
            }

            if (f1 == seq.get(i)) {
                int j = i;
                while (j < seq.size() && f1 == seq.get(j)) {
                    j++;
                    count++;
                    fd = f1 + f2;
                    f2 = f1;
                    f1 = fd;
                }
                if (count > maxcount)
                    maxcount = count;

                j--;
                i = j;
            }
            // надо закинуть i в j
        }
        return maxcount;
    }

    public int getNextPos(int k) {
        //System.out.println("начал искать подпоследовательность");
        for (int j = k; j < seq.size(); j++) { // вернет указатель на первый эл-т, который может начинать новую пос-ть
            //System.out.println("ищу с номера " + j + ":");
            if (seq.size() > j + 1 && seq.get(j) == 1 && seq.get(j + 1) == 1 && maxlen == 2) {
                //System.out.println("нашел 1,1! длинна = 2 , вернул " + (j+1));
                return (j + 1);
            }

            int f1 = 1, f2 = 1, fd, count = 0;
            int i = j;

            if (seq.size() > i + 1 && seq.get(i) == 1 && seq.get(i + 1) == 1) {
                //System.out.println("узнал, что начинается с 1,1, поменял а2 на 0");
                f2 = 0;
            }

            while ((seq.get(i)) > f1) {
                fd = f1 + f2;
                f2 = f1;
                f1 = fd;
            }

            if (seq.get(i) == f1) {
                //System.out.println("начал последовательно сравнивать");
                // начинаем последовательно сравнивать seq и фибоначи
                while (i < seq.size() && seq.get(i) == f1) {
                   // System.out.println("сравнил " + i + "-й элемент, подошло");
                    count++;
                    fd = f1;
                    f1 += f2;
                    f2 = fd;
                    i++;
                }
               // System.out.println("а вот" + i + "-й не подошел(или seq кончился)");
                if (count == maxlen) {
                    //System.out.println("возвращаю " + i);
                    return i;
                }
               // System.out.println("откатил j на -1");
                j = i-1;
            }
        }
        return -1;
    }

    public Iterator<Integer> iterator() {
        return new SeqIterator();
    }

    private class SeqIterator implements Iterator<Integer> {
        private int pos; // указатель на элемент последовательности,
        // который потенциально может стать началом новой подпоследовательности

        public SeqIterator() {
            pos = 0;
        }


        public boolean hasNext() {
            //System.out.println("не важно {");
            if (getNextPos(pos) == -1) {
                //System.out.println("end!");
                return false;
            }
            //System.out.println("}");
           // System.out.println();
            return true;
        }

        public Integer next() { // вернет указатель на эл-т, стоящий после конца
            pos = getNextPos(pos); // в pos записали указатель на эл-т, который может начать новую последовательность
           // System.out.println("next: записал " + pos + " в pos " );
            //System.out.print("getNextPos" + (pos) + ": ");
            if(maxlen == 2 && pos >= 1 && seq.get(pos-1) == 1 && seq.get(pos) == 1){
                //System.out.println("next: возвращаю " + (pos-1) + "на вывод" );
                //System.out.println();
                return pos-maxlen+1;
            }
           // System.out.println("next: возвращаю " + pos + "на вывод" );
           // System.out.println();
            return pos-maxlen;
        }

    }

    public String toString() {
        String s = "";
        for (int x : seq) {
            s += Integer.toString(x) + " ";
        }
        return s;
    }
}

