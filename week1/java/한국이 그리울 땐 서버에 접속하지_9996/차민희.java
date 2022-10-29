import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _9996_when_miss_korea_connect_to_server {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] pattern = br.readLine().split("\\*");
        String fname;
        for (int i=0; i<n; i++) {
            fname = br.readLine();
            if (fname.length() < pattern[0].length() + pattern[1].length()) {
                System.out.println("NE");
                continue;
            }
            if (fname.startsWith(pattern[0]) && fname.endsWith(pattern[1])) {
                System.out.println("DA");
            } else {
                System.out.println("NE");
            }
        }
    }
}
