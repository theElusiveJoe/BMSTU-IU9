import java.util.Optional;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Sequence {

    int num;

    int getNum(int x) {
        num++;
        return x * num;
    }

    Integer getNum2(int x) {
        num++;
        if (x >= 0)  return num;
        return 0;
    }


    IntStream showNums(int[] a) {
        num = 0;
        return IntStream.of(a).flatMap(x -> Stream.iterate(x, y -> y / 2)
                    .limit(32)
                    .mapToInt(Integer::intValue))
                .map(x -> x % 2)
                .map(x -> getNum(x))
                .filter(x -> x > 0);
    }

    Optional<Integer> findX(int[] a) {
        num = 0;
        int bitSum = IntStream.of(a)
                .reduce((acc, x) -> (acc | x))
                .getAsInt();
        Optional<Integer> num = IntStream.of(a)
                .map(x -> x-bitSum)
                .map(x -> getNum2(x))
                .filter(x -> x > 0)
                        .boxed()
                        .findFirst();
        return num;
    }
}
