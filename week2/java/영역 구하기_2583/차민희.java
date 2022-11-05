import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class _2583_calc_area {
    static boolean[][] area;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        area = new boolean[m][n];
        int x1, y1, x2, y2;
        for (int i=0; i<k; i++) {
            st = new StringTokenizer(br.readLine());
            x1 = Integer.parseInt(st.nextToken());
            y1 = Integer.parseInt(st.nextToken());
            x2 = Integer.parseInt(st.nextToken());
            y2 = Integer.parseInt(st.nextToken());
            for (int x=x1; x<x2; x++) {
                for (int y=y1; y<y2; y++) {
                    area[x][y] = true;
                }
            }
        }
        List<Integer> size = new ArrayList<>();
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (!area[i][j]) {
                    cnt = 1;
                    area[i][j] = true;
                    dfs(i, j);
                    size.add(cnt);
                }
            }
        }
        Collections.sort(size);
        StringBuilder sb = new StringBuilder();
        sb.append(size.size());
        sb.append("\n");
        for (int i=0; i<size.size(); i++) {
            sb.append(size.get(i));
            if (i != k-1) {
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());
    }

    static int cnt;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};
    private static void dfs(int x, int y) {
        int nx, ny;
        for (int i=0; i<4; i++) {
            nx = x+dx[i];
            ny = y+dy[i];
            if (nx >= 0 && nx < area.length && ny >= 0 && ny < area[0].length
                    && !area[nx][ny]) {
                cnt++;
                area[nx][ny] = true;
                dfs(nx, ny);
            }
        }
    }
}
