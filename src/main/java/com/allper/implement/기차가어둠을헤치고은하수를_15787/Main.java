package com.allper.implement.기차가어둠을헤치고은하수를_15787;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

/**
 * packageName    : allper.implement.기차가어둠을헤치고은하수를_15787
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-29        ipeac       최초 생성
 */
public class Main {
    
    static int[][] trains;
    static boolean[] visited;
    static int ans;
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        int n = rd.nextInt();
        trains = new int[n + 1][n + 1];
        int m = rd.nextInt();
        for (int i = 0; i < m; i++) {
            int function = rd.nextInt();
            if (function == 1) {
                int train = rd.nextInt(); // i번째
                int seat = rd.nextInt(); // 번째 좌석
                if (trains[train][seat] == 0) { // 비어있으면
                    trains[train][seat] = 1;
                }
            } else if (function == 2) {
                int train = rd.nextInt(); // i번째
                int seat = rd.nextInt(); // 번째 좌석
                if (trains[train][seat] == 1) {
                    trains[train][seat] = 0;
                }
            } else if (function == 3) {
                int train = rd.nextInt(); // i번째
                for (int j = trains[train].length - 1; j > 1; j--) {
                    trains[train][j] = trains[train][j - 1];
                }
                trains[train][1] = 0;
            } else {
                int train = rd.nextInt(); // 번째
                for (int j = 1; j < trains[train].length - 2; j++) {
                    trains[train][j] = trains[train][j + 1];
                }
                trains[train][trains[train].length - 1] = 0;
            }
        }
        Set<String> set = new HashSet<>();
        for (int i = 1; i <= n; i++) {
            set.add(Arrays.toString(trains[i]));
        }
        System.out.println(set.size());
    }
    
    static boolean checkVisited(int[] train) {
        for (int i = 1; i < train.length - 1; i++) {
            if (visited[i]) {
                return false;
            }
        }
        return true;
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
