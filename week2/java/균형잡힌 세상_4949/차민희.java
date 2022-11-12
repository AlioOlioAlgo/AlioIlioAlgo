import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class _4949_balanced_world {
	static StringBuilder sb = new StringBuilder();
	static final String YES = "yes\n";
	static final String NO = "no\n";
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		while ((line = br.readLine()) != null) {
			if (line.equals(".")) {
				break;
			}
			solution(line);
		}
		System.out.println(sb);
	}
	
	private static void solution(String line) {
		Stack<Character> stack = new Stack<>();
		for (char c : line.toCharArray()) {
			if (c != '(' && c != ')' && c != '[' && c!= ']') {
				continue;
			}
			if (stack.isEmpty() && (c == ')' || c == ']')) {
				sb.append(NO);
				return;
			}
			if (c == ')' && !stack.isEmpty() && stack.peek() == '('
					|| c == ']' && !stack.isEmpty() && stack.peek() == '[') {
				stack.pop();
			} else {
				stack.push(c);
			}
		}
		if (stack.isEmpty()) {
			sb.append(YES);
		} else {
			sb.append(NO);
		}
	}
}
