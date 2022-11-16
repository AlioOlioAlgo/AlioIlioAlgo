import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _2636_cheese {
    static int[][] map;
    static int n, m;
    static Queue<int[]> queue = new LinkedList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        edge();
        int cheese = 0, time = 0;
        int size;
        while (!queue.isEmpty()) {
            time++;
            cheese = queue.size();
            size = cheese;
            while (size-- > 0) {
                int[] e = queue.poll();
                melt(e[0], e[1]);
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(time);
        sb.append("\n");
        sb.append(cheese);
        System.out.println(sb);
    }

    private static void edge() {
        map[0][0] = -1; //방문 체크
        melt(0, 0);
    }

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    private static void melt(int x, int y) {
        int nx, ny;
        for (int i=0; i<4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            if (map[nx][ny] == 0) {
                map[nx][ny] = -1; //방문 표시
                melt(nx, ny);
            } else if (map[nx][ny] == 1) {
                map[nx][ny] = 2;
                queue.offer(new int[]{nx, ny});
            }
        }
    }
}
