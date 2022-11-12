import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1436_film_director {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		solution(N);
	}
	
	private static void solution(int N) {
		int n = 1;
		int result = 666;
		while (n < N) {
			if (String.valueOf(++result).contains("666")) {
				n++;
			}
		}
		System.out.println(result);
	}
}
