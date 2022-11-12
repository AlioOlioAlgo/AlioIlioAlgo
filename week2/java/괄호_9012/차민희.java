import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class _9012_parenthesis {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for  (int i=0; i<t; i++) {
			solution(br.readLine());
		}
	}
	
	private static void solution(String line) {
		Stack<Character> stack = new Stack<>();
		for (char c : line.toCharArray()) {
			if (stack.isEmpty() && c == ')') {
				System.out.println("NO");
				return;
			}
			if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
				stack.pop();
			} else {
				stack.push(c);
			}
		}
		if (stack.isEmpty()) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}
	}
}
