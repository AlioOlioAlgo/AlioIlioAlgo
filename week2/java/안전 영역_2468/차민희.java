import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class _2468_safe_area {
    static int[][] zone;
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        zone = new int[n][n];
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++) {
                zone[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int max = 1;
        boolean[][] visited;
        for (int h=1; h<=100; h++) {
            visited = new boolean[n][n];
            int cnt = count(visited, h);
            if (cnt > max) {
                max = cnt;
            }
        }
        System.out.println(max);
    }

    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};
    private static int count(	boolean[][] visited,
                                 int height) {
        int cnt = 0;
        for (int i=0; i<visited.length; i++) {
            for (int j=0; j<visited.length; j++) {
                if (!visited[i][j] && zone[i][j] > height) {
                    cnt++;
                    dfs(visited, i, j, height);
                }
            }
        }
        return cnt;
    }

    private static void dfs(boolean[][] visited,
                            int x,
                            int y,
                            int height) {
        visited[x][y] = true;
        int nx;
        int ny;
        for (int k=0; k<4; k++) {
            nx = x+dx[k];
            ny = y+dy[k];
            if (nx >= 0 && nx < visited.length && ny >= 0 && ny < visited.length
                    && !visited[nx][ny] && zone[nx][ny] > height) {
                dfs(visited, nx, ny, height);
            }
        }
    }
}
