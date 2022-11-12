import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1436_film_director2 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		solution(N);
	}

	private static void solution(int N) {
		int n = 0;
		int pre = 0; //앞의 4자리
		while (true) {
			if (pre / 10 == 666 || pre % 1000 == 666) { // 666x|xxx, x666|xxx
				for (int i=0; i<1000; i++) { //뒤의 3자리
					n++;
					if (n == N) {
						System.out.println(pre * 1000 + i);
						return;
					}
				}
			} else if (pre % 100 == 66) { // xx66|6xx
				for (int i=600; i<700; i++) {
					n++;
					if (n == N) {
						System.out.println(pre * 1000 + i);
						return;
					}
				}
			} else if (pre % 10 == 6) { // xxx6|66x
				for (int i=660; i<670; i++) {
					n++;
					if (n == N) {
						System.out.println(pre * 1000 + i);
						return;
					}
				}
			} else {	// xxxx|666
				n++;
				if (n == N) {
					System.out.println(pre * 1000 + 666);
					return;
				}
			}
			pre++;
		}
	}
}
