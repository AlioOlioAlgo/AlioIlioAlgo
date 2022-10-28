import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _4375_1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        int n;
        while ((line = br.readLine()) != null) {
            n = Integer.parseInt(line);
            System.out.println(one(n, 1 % n,1));
        }
    }

    /**
     * @param n 입력받은 수
     * @param r 나머지
     * @param d 자릿수
     * @return
     */
    public static int one(int n, int r, int d) {
        if (r % n == 0) {
            return d;
        }
        return one(n, (r * 10 + 1) % n, d+1);
    }
}
