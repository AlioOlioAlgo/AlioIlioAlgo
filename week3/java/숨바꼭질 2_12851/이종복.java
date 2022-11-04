import java.util.*;

public class Main {
    
    public static int N;
    public static int K;
    public static int[] count; 
    public static int minCnt; 
    public static int answer; 
    
    
    
    public static boolean isInside(int x){
        if(0<=x && x <= 100000){
            return true;
        }else{
            return false; 
        }
    }
    
    public static void BFS(int start){
        
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        
        count[start] = 1;
        
        while(!q.isEmpty()){
            
            int curr = q.poll();
            
            if(count[curr] > minCnt){
                continue;
            }
            
            if(curr == K){
                
                minCnt = Math.min(minCnt, count[curr]);
                
                if(minCnt == count[curr]){
                    answer++; 
                }
            }
            
            
            for(int i=0; i<3; i++){
                
                int next = 0;
                
                if(i == 0) next = curr-1;
                if(i == 1) next = curr+1;
                if(i == 2) next = curr*2;
                
                if(!isInside(next)) continue;
                
                if(count[next] == 0 || count[next] == count[curr] + 1){
                    count[next] = count[curr] + 1;
                    q.add(next); 
                }
                 
                
            }
            
            
        }
        
        
        
        
    }
    
    
    
    
    
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in);
      
      count = new int[100010];
      
      minCnt = Integer.MAX_VALUE; 
      
      answer = 0; 
      
      N = sc.nextInt();
      K = sc.nextInt(); 
      
      BFS(N);
      
      System.out.println(count[K]-1);
      System.out.println(answer);
      
      
      
      
      
    }
}
