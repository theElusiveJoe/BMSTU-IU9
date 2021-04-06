import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) {
        int[] A = {1, 2, 15, 9};
        int[] B = {1,2,4,8};
        Sequence seq = new Sequence();

        List la = seq.showNums(A).boxed().collect(Collectors.toList());
        System.out.println(la);
        int bitsAmmount = IntStream.of(A).flatMap(x -> Stream.iterate(x, y -> y / 2)
                .limit(32)
                .mapToInt(Integer::intValue))
                .map(x -> x % 2)
                .sum();
        if (la.size() == bitsAmmount){
            System.out.println("Correct)");
        } else {
            System.out.println("Not correct(");
        }

        System.out.println();
        Optional positiv;
        positiv = seq.findX(A);
        if(!positiv.isEmpty()){
            System.out.println(positiv.get());
        } else {
            System.out.println("No such X");
        }

        System.out.println();
        positiv = seq.findX(B);
        if(!positiv.isEmpty()){
            System.out.println(positiv.get());
        } else {
            System.out.println("No such X");
        }
    }
}
