package com.allper.functions.배열돌리기;

import java.io.*;
import java.util.StringTokenizer;

/**
 * packageName    : allper.functions.배열돌리기
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-21        ipeac       최초 생성
 */
public class Main {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, m, r;
    
    static Integer[][] graph;
    
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        graph = new Integer[n][m];
        
        for (int i = 0; i < n; i++) {
            String[] line = bf.readLine()
                                    .split(" ");
            Integer[] input = new Integer[m];
            for (int j = 0; j < m; j++) {
                input[j] = Integer.parseInt(line[j]);
            }
            graph[i] = input;
        }
        for (int i = 0; i < r; i++) {
            rotate();
        }
        
        for (Integer[] integers : graph) {
            for (Integer integer : integers) {
                bw.write(integer + " ");
            }
            bw.newLine();
        }
        
        bf.close();
        bw.flush();
        bw.close();
    }
    
    public static void rotate() throws IOException {
        int layers = Math.min(n, m) / 2;
        for (int layer = 0; layer < layers; layer++) {
            int rowEnd = n - layer - 1;
            int colEnd = m - layer - 1;
            
            //
            int tempValue = graph[layer][colEnd];
            //right up
            for (int i = layer; i < rowEnd; i++) {
                graph[i][colEnd] = graph[i + 1][colEnd];
            }
            // down right
            for (int i = colEnd; i > layer; i--) {
                graph[rowEnd][i] = graph[rowEnd][i - 1];
            }
            //left  down
            for (int i = rowEnd; i > layer; i--) {
                graph[i][layer] = graph[i - 1][layer];
            }
            // top left
            for (int i = layer; i < colEnd; i++) {
                graph[layer][i] = graph[layer][i + 1];
            }
            graph[layer][colEnd - 1] = tempValue;
            
        }
        
    }
    
    public static <T> void print(T[][] param) throws IOException {
        bw.write("========================================\n");
        for (T[] ts : param) {
            for (T t : ts) {
                bw.write(t + " ");
            }
            bw.newLine();
        }
        bw.write("========================================");
        
    }
    
    
}
