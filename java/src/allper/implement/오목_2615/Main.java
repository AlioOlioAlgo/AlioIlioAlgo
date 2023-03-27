package allper.implement.오목_2615;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * packageName    : allper.implement.오목_2615
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-27        ipeac       최초 생성
 */
class Pos {
    int x;
    int y;
    
    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Main {
    static int[][] graph;
    static int[][] moves = {{0, 1}, {1, 1}, {1, 0}, {-1, 1}};
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        graph = new int[19][19];
        for (int i = 0; i < 19; i++) {
            String input = rd.nextLine();
            for (int j = 0, index = 0; j < 19; index += 2, j++) {
                graph[i][j] = Character.getNumericValue(input.charAt(index));
            }
        }
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                if (graph[i][j] != 0) {
                    for (int k = 0; k < 4; k++) {
                        if (lineDrive(i, j, k) == 5) {
                            int[] dir = moves[k];
                            //만약 5개 를 충족하였더라도 반대 방향에 해당 값과 동일한 값이 있으면 안됩니다.
                            if (inRange(i - dir[0], j - dir[1]) && graph[i][j] == graph[i - dir[0]][j - dir[1]]) {
                                continue;
                            }
                            if (graph[i][j] == 1 || graph[i][j] == 2) {
                                System.out.println(graph[i][j]);
                                System.out.println((i + 1) + " " + (j + 1));
                                System.exit(0);
                                
                            }
                        }
                    }
                }
            }
        }
        System.out.println(0);
    }
    
    public static int lineDrive(int x, int y, int dir) {
        int count = 1;
        int[] moveD = moves[dir];
        int nx = x + moveD[0], ny = y + moveD[1];
        
        while (inRange(nx, ny) && graph[nx][ny] == graph[x][y]) {
            count++;
            nx += moveD[0];
            ny += moveD[1];
        }
        return count;
    }
    
    public static boolean inRange(int x, int y) {
        return 0 <= x && x < 19 && 0 <= y && y < 19;
    }
    
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine(), " ");
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
        
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
