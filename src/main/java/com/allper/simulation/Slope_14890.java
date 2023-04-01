package com.allper.simulation;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * packageName    : allper.simulation
 * fileName       : Slope
 * author         : ipeac
 * date           : 2023-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-19        ipeac       최초 생성
 */
public class Slope_14890 {
    static int n, l;
    static int[][] graph;
    static boolean[] visited; // 경사로 이미 놓아진적있으면 안되니까
    
    static int ans;
    
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());
        
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            graph[i] = Arrays.stream(bf.readLine()
                                             .split(" "))
                               .mapToInt(Integer::parseInt)
                               .toArray();
        }

//        prettyPrintMatrix(graph);
//        bw.write("========================================");
        // 가로 그래프 체크
        for (int[] ints : graph) {
            if (check_slope(ints)) {
                ans++;
            }
        }
        // 세로 그래프 체크
        for (int i = 0; i < n; i++) {
            int[] columns = new int[n];
            for (int j = 0; j < n; j++) {
                columns[j] = graph[j][i];
            }
            if (check_slope(columns)) {
                ans++;
            }
        }
        bw.write(String.valueOf(ans));
        
        bw.flush();
        bw.close();
    }
    
    public static boolean inRange(int x) {
        return 0 <= x && x < n;
    }
    
    public static boolean check_slope(int[] lines) {
        visited = new boolean[n];
        for (int i = 0; i < n - 1; i++) {
            if (Math.abs(lines[i] - lines[i + 1]) >= 2) {
                // 해당 길은 2이상 차이나기에 안됨
                return false;
            }
            //내리막길 체크
            if (lines[i] - lines[i + 1] == 1) {
                for (int j = 1; j <= l; j++) {
                    //경사로 인정 길이 만큼 생각
                    if (!inRange(i + j) || lines[i + 1] != lines[i + j] || visited[i + j]) {
                        return false;
                    }
                    visited[i + j] = true;
                }
            }
            //오르막길 체크
            if (lines[i + 1] - lines[i] == 1) {
                for (int j = 0; j < l; j++) {
                    //경사로 인정 길이 만큼 생각
                    if (!inRange(i - j) || lines[i] != lines[i - j] || visited[i - j]) {
                        return false;
                    }
                    visited[i - j] = true;
                }
            }
        }
        
        return true;
    }
    
    public static void prettyPrintMatrix(int[][] matrix) throws IOException {
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                bw.write(String.valueOf(matrix[i][j]));
                
                // Add spacing between elements
                if (j < cols - 1) {
                    bw.write(" ");
                }
            }
            // Start a new line for the next row
            bw.newLine();
        }
    }
}
