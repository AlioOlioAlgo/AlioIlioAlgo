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
public class Main {
    static int[][] graph;
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        graph = new int[19][19];
        for (int i = 0; i < 19; i++) {
            int[] line = new int[19];
            for (int j = 0; j < 19; j++) {
                line[i] = rd.nextInt();
            }
            graph[i] = line;
        }
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
                    st = new StringTokenizer(br.readLine());
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
