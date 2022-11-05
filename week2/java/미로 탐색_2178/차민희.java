import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class _2178_maze_exploration {
    static int n;
    static int m;
    static boolean[][] maze;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maze = new boolean[n][m];
        for (int i=0; i<n; i++) {
            String line = br.readLine();
            for (int j=0; j<m; j++) {
                maze[i][j] = line.charAt(j) == '1';
            }
        }
        visited = new boolean[n][m];
        visited[0][0] = true;
        int dist = exploration(0, 0, 1);
        System.out.println(dist);
    }

    /**
     * @param x 현재위치 아래좌표
     * @param y 현재위치 오른좌표
     * @param dist 거리
     */
    private static int exploration(int x, int y, int dist) {
        Queue<int[]> queue = new LinkedList<>();
        int dx[] = {1, 0, 0, -1};
        int dy[] = {0, 1, -1, 0};
        queue.offer(new int[]{x, y, dist});
        while (true) {
            int[] curr = queue.poll();
            x = curr[0];
            y = curr[1];
            dist = curr[2];
            if (x == n-1 && y == m-1) {
                return dist;
            }
            for (int i=0; i<4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m
                && maze[nx][ny] && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, dist+1});
                }
            }
        }
    }
}
