import java.util.*;

public class Main {
    
    public static int[] arr;
    
    public static void main(String args[]) {
        Main T = new Main();
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        
        int[] arr = new int[110];
        
        for (int i = 0; i < 3; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            
            for (int j = start; j < end; j++) {
                arr[j] += 1;
            }
        }
        
        for (int i = 1; i <= 100; i++) {
            if (arr[i] == 0) {
                continue;
            } else if (arr[i] == 1) {
                sum += A;
            } else if (arr[i] == 2) {
                sum += 2 * B;
            } else if (arr[i] == 3) {
                sum += 3 * C;
            }
        }
        
        System.out.println(sum);
        
    }
}
