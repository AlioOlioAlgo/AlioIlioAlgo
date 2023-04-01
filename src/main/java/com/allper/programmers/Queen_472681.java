package com.allper.programmers;

import java.io.*;

/**
 * packageName    : allper.simulation
 * fileName       : Queen_472681
 * author         : ipeac
 * date           : 2023-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-21        ipeac       최초 생성
 */
public class Queen_472681 {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    static int[] board;
    static int answer;
    
    public static int solution(int n) {
        board = new int[n];
        
        placeQueen(n, 0);
        return answer;
    }
    
    public static void placeQueen(int n, int row) {
        if (row == n) {
            answer++;
            return;
        }
        for (int i = 0; i < n; i++) {
            board[row] = i;
            if (isPossible(row)) {
                placeQueen(n, row + 1);
            }
        }
    }
    
    private static boolean isPossible(int row) {
        for (int i = 0; i < row; i++) {
            // 같은 열일때 절대 안됨!
            if (board[i] == board[row]) {
                return false;
            }
            //대각선이 겹치는지 체크합니다
            if (Math.abs(row - i) == Math.abs(board[row] - board[i])) {
                return false;
            }
        }
        return true;
    }
    
    public static void main(String[] args) throws IOException {
        bw.write(solution(4) + "\n");
        bf.close();
        bw.flush();
        bw.close();
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
