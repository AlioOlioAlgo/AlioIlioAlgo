package allper.programmers;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * packageName    : allper.programmers
 * fileName       : Hanoi_472725
 * author         : ipeac
 * date           : 2023-03-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-21        ipeac       최초 생성
 */
public class Hanoi_472725 {
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    static List<int[]> moves;
    
    public static int[][] solution(int n) {
        list = new ArrayList<>();
        int[][] answer = new int[][];
        
        return answer;
    }
    
    public static void hanoi(int n, int from, int temp, int to) {
        if (n == 0) {
            return;
        }
        hanoi(n - 1, from, to, temp);
        
    }
    
    
    public static void main(String[] args) throws IOException {
        System.out.println(Arrays.deepToString(solution(2)));
        bw.write("========================================");
        
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
