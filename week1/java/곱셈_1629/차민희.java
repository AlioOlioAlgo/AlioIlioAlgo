import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

public class _1629_multiply {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        // 10 11 12
        long result = 1;
        long n = nums[0];
        while (nums[1] > 0) {
            if (nums[1] % 2 == 1) {
                result = result * n % nums[2];
            }
            nums[1] /= 2;
            n = n * n % nums[2];
        }
        System.out.println(result);
    }
}
