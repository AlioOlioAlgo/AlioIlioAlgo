import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class _1159_basketball_game {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int[] cnt = new int[26];
        for (int i=0; i<num; i++) {
            cnt[br.readLine().charAt(0) - 'a']++;
        }
        boolean isPREDAJA = true;
        StringBuffer sb = new StringBuffer();
        for (int i=0; i<cnt.length; i++) {
            if (cnt[i] >= 5) {
                sb.append((char)(i+'a'));
                isPREDAJA = false;
            }
        }
        if (isPREDAJA) {
            System.out.println("PREDAJA");
        } else {
            System.out.println(sb.toString());
        }
    }
}
