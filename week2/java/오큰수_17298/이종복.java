import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Stack;

public class Main {
    public static void main(String args[]) throws IOException {
     	
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> stk = new Stack<Integer>();
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N+10];
		
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		for(int i = 1; i <= N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
 
      
        	for(int i=1; i<=N; i++){
          
          
          		while(!stk.isEmpty() && arr[stk.peek()] < arr[i]){
              			arr[stk.pop()] = arr[i];
          		}
          
         
          	stk.push(i);
       		}
      
      
      while(!stk.isEmpty()){
          arr[stk.pop()] = -1; 
      }
      
      
      	
		StringBuilder sb = new StringBuilder();
		for(int i = 1; i <= N; i++) {
			sb.append(arr[i]).append(' ');
		}
		
		System.out.println(sb);
      
      
      
      
    }
}
