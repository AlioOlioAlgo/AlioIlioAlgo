import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1213_create_palindrome {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String name = br.readLine();
        int[] cnts = new int[26];
        for (char c : name.toCharArray()) {
            cnts[c-'A']++;
        }
        Character odd = null;
        for (int i=0; i<cnts.length; i++) {
            if (cnts[i] % 2 == 1) {
                if (odd != null) {
                    System.out.println("I'm Sorry Hansoo");
                    return;
                }
                odd = (char)(i + 'A');
            }
        }
        char[] palindrome = new char[name.length()];
        //AABCBAA
        if (odd != null) {
            palindrome[name.length()/2] = odd;
            cnts[odd-'A']--;
        }
        int i = 0;
        int c = 0;
        while (i < name.length()/2) {
            int half = cnts[c]/2;
            while (half-- > 0) {
                palindrome[i] = (char)(c + 'A');
                palindrome[name.length()-1-i] = (char)(c + 'A');
                i++;
            }
            c++;
        }
        System.out.println(String.valueOf(palindrome));
    }
}
