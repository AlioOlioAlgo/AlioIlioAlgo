import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _1012_organic_cabbage {
    static BufferedReader br;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            cntEarthworm();
        }
    }

    private static void cntEarthworm() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        boolean[][] map = new boolean[m][n];
        for (int i=0; i<k; i++) {
            st = new StringTokenizer(br.readLine());
            map[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = true;
        }
        Queue<int[]> queue = new LinkedList<>();
        int cnt = 0;
        int[] dx = {0, 0, -1, 1};
        int[] dy = {1, -1, 0, 0};
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (queue.isEmpty() && map[i][j]) {
                    queue.offer(new int[]{i, j});
                    map[i][j] = false;
                    cnt++;
                }
                while (!queue.isEmpty()) {
                    int[] xy = queue.poll();
                    int x = xy[0];
                    int y = xy[1];
                    for (int t=0; t<4; t++) {
                        int nx = x + dx[t];
                        int ny = y + dy[t];
                        if (nx >=0 && nx < m && ny >= 0 && ny < n
                            && map[nx][ny]) {
                            queue.offer(new int[]{nx, ny});
                            map[nx][ny] = false;
                        }
                    }
                }
            }
        }
        System.out.println(cnt);
    }
}
