package com.allper.simulation;

import java.io.*;

/**
 * packageName    : allper.simulation
 * fileName       : StartAndLink
 * author         : ipeac
 * date           : 2023-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-19        ipeac       최초 생성
 */
public class StartAndLink {
    
    private static int n;
    private static int minAns = Integer.MAX_VALUE;
    private static int[][] graph;
    private static boolean[] visited;
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(bf.readLine());
        
        graph = new int[n][n];
        visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            String[] ele = bf.readLine()
                                   .split(" ");
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(ele[j]);
            }
        }
        dfs(0, 0);
        bw.write(String.valueOf(minAns));
        
        bf.close();
        bw.flush();
        bw.close();
    }
    
    public static void dfs(int cur, int depth) {
        if (depth == n / 2) {
            getMinDiff();
        }
        for (int next = cur; next < n; next++) {
            if (!visited[next]) {
                visited[next] = true;
                dfs(next, depth + 1);
                visited[next] = false;
            }
        }
    }
    
    private static void getMinDiff() {
        int start = 0, end = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (visited[i] && visited[j]) {
                    start += graph[i][j];
                    start += graph[j][i];
                } else if (!visited[i] && !visited[j]) {
                    end += graph[i][j];
                    end += graph[j][i];
                }
            }
        }
        minAns = Math.min(minAns, Math.abs(start - end));
    }
    
    public static void prettyPrintMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j]);
                
                // Add spacing between elements
                if (j < cols - 1) {
                    System.out.print(" ");
                }
            }
            // Start a new line for the next row
            System.out.println();
        }
    }
    
    
}
