import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2852_nba_basketball {
    static int end;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        end = 2880;
        int aWin = 0, bWin = 0;
        int score =  0;
        int time = 0, preTime = 0;
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            int team = Integer.parseInt(st.nextToken());
            preTime = time;
            time = getSec(st.nextToken());
            if (score > 0) {
                aWin += time - preTime;
            } else if (score < 0) {
                bWin += time - preTime;
            }
            if (team == 1) {
                score++;
            } else {
                score--;
            }
        }
        if (score > 0) {
            aWin += end - time;
        } else if (score < 0) {
            bWin += end - time;
        }
        System.out.println(String.format("%02d:%02d", aWin / 60, aWin % 60));
        System.out.println(String.format("%02d:%02d", bWin / 60, bWin % 60));
    }
    private static int getSec(String time) {
        String[] tmp = time.split(":");
        int sec = 0;
        sec += Integer.parseInt(tmp[0]) * 60;
        sec += Integer.parseInt(tmp[1]);
        return sec;
    }
}
