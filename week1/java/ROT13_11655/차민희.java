import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _11655_ROT13 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c >= 'A' && c < 'N' || c >= 'a' && c < 'n') {
                c += 13;
            } else if (c >= 'N' && c <= 'Z' || c >= 'n' && c <= 'z') {
                c -= 13;
            }
            sb.append(c);
        }
        System.out.println(sb.toString());
    }
}
