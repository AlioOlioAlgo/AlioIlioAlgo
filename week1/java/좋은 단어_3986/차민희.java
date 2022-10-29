import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class _3986_good_word {
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++) {
            goodWord(br.readLine());
        }
        System.out.println(cnt);
    }

    public static void goodWord(String word) {
        if (word.length() % 2 == 1) {
            return;
        }
        Stack<Character> stack = new Stack<>();
        for (char c : word.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        if (stack.isEmpty()) {
            cnt++;
        }
    }

    /**
2
ABABBABA
ABABBABABBAA
-
2
     */
}
