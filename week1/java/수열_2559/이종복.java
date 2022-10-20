import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      int N = sc.nextInt();
      int K = sc.nextInt();
      int[] arr = new int[100010];
      
      for(int i=0; i<N; i++){
          arr[i] = sc.nextInt();
      }
      
      int maxSum = Integer.MIN_VALUE; 
      
      for(int i=0; i<=N-K; i++){
          int sum = 0;
          
          for(int j=i; j<=(i+K-1); j++){
              sum += arr[j];
          }
          
          maxSum = Math.max(maxSum, sum);
      }
      
      
      System.out.println(maxSum); 
    }
    
}
