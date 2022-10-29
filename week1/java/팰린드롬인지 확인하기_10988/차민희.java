import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _10988_determine_palindrome {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        for (int i=0; i<word.length()/2; i++) {
            if (word.charAt(i) != word.charAt(word.length()-i-1)) {
                System.out.println(0);
                return;
            }
        }
        System.out.println(1);
    }
}
