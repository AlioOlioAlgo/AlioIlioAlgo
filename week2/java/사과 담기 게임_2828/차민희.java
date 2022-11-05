import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2828_apple_picking_game {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int cnt = Integer.parseInt(br.readLine());
        int start = 1;
        int end = m;
        int where;
        int sum = 0;
        int dist = 0;
        for (int i=0; i<cnt; i++) {
            where = Integer.parseInt(br.readLine());
            if (where > end) {
                dist = where - end;
                sum += dist;
                end = where;
                start += dist;
            } else if (where < start) {
                dist = start - where;
                sum += dist;
                start = where;
                end -= dist;
            }
        }
        System.out.println(sum);
    }
}
