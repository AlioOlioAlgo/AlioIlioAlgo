package allper.functions;

import java.io.*;
import java.util.StringTokenizer;

/**
 * packageName    : allper.functions
 * fileName       : gamesUsingFunctions
 * author         : ipeac
 * date           : 2023-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-19        ipeac       최초 생성
 */
public class GamesUsingFunctions {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        int ans = 0;
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        // 3 ,6, 9 중에 하나가 들어있는 경우
        for (int num = a; num <= b; num++) {
            String string = String.valueOf(num);
            if (string.contains("3") || string.contains("6") || string.contains("9") || Integer.parseInt(string) % 3 == 0) {
                ans++;
            }
        }
        bw.write(String.valueOf(ans));
        bw.flush();
        bf.close();
        bw.close();
    }

}
