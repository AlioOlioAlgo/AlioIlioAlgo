package allper;

import java.util.Arrays;
import java.util.List;

/**
 * packageName    : allper
 * fileName       : Stream1
 * author         : ipeac
 * date           : 2023-02-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-26        ipeac       최초 생성
 */
public class Stream1 {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("orange", "apple", "banana", "lemon", "pear", "watermelon");
        List<Integer> result = words.stream()
                .map(String::length)
                .sorted()
                .toList();
        System.out.println("result = " + result);
    }
}
