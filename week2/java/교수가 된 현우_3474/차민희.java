import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _3474_professor_hyeon_woo {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            count(Integer.parseInt(br.readLine()));
        }
        System.out.println(sb.toString());
    }

    private static void count(int num) {
        int multiple = 5;
        int quotient = num / multiple;
        int cnt = 0;
        while (quotient > 0) {
            cnt += quotient;
            multiple *= 5;
            quotient = num / multiple;
        }
        sb.append(cnt);
        sb.append("\n");
    }
}
