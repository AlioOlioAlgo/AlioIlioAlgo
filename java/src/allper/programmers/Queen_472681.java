package allper.programmers;

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
    
    static private
    
    static class Solution {
        public int solution(int n) {
            int answer = 0;
            
            return answer;
        }
        
        public void placeQueen() {
        
        }
    }
    
    public static void main(String[] args) throws IOException {
        Solution solution = new Solution();
        bw.write(solution.solution(4) + "\n");
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
