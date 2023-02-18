package allper;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

/**
 * packageName    : allper
 * fileName       : jav
 * author         : ipeac
 * date           : 2023-02-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-12        ipeac       최초 생성
 */
public class Jav {

    static List<Integer> arr = new ArrayList<>();

    static List<Boolean> visited;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(input.readLine());
        System.out.println("n = " + n);
        
        makePermutations(0);
    }

    public static void makePermutations(int cnt) {
        if (cnt == n) {
            printArr();
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited.get(i)) {
                arr.add(i);
                visited.set(i, true);
                makePermutations(cnt + 1);
                arr.remove(arr.size() - 1);
                visited.set(i, false);
            }
        }
    }

    public static void printArr() {
        for (int value : arr) {
            System.out.print(value + " ");
        }
    }
}
