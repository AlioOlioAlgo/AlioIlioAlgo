import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class _2559_sequence {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] nums = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        //3 | -2 | -4 | -9 | 0 | 3 | 7 | 13 | 8 | -3
        int sum = 0;
        for (int i=0; i<k; i++) {
            sum += nums[i];
        }
        int max = sum;
        for (int i=k; i<n; i++) {
            sum += nums[i] - nums[i-k];
            if (sum > max) {
                max = sum;
            }
        }
        System.out.println(max);
    }
}
