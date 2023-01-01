import java.util.*; 

public class Main {
    
    
    public static int N;
    public static int K; 
    public static int time; 
    public static boolean[][] visited; 
    public static boolean find; 
    
    
    public static boolean isInside(int x){
        if(0<=x && x<=500000){
            return true;
        }else{
            return false; 
        }
    }
    
    public static void BFS(int start){
        
        
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        
        
        while(true){
            
            if(K > 500000){
                find = false;  
                break;
            }
            
            int len = q.size();
            
            time++; 
            
            int pos = 0;
            if(time % 2 == 0){
                pos = 0;
            }else{
                pos = 1; 
            }
            
            
            
            for(int i=0; i<len; i++){
                
                int curr = q.poll();
                int next = 0; 
                
                for(int j=0; j<3; j++){
                    if(j == 0) next = curr-1;
                    if(j == 1) next = curr+1;
                    if(j == 2) next = curr*2; 
                    
                    if(!isInside(next)){
                        continue;
                    }
                    
                    if(visited[pos][next] == false){
                        // System.out.println("pos, next는?" + pos + " "  + next); 
                        visited[pos][next] = true; 
                        q.add(next); 
                    }
                    
                }
                
                
            }
            
            
            K += time;
            
            
            // System.out.println("time, pos, K는?" + time + " " + pos + " " + K);
            // System.out.println(visited[pos][K]);
            // System.out.println(time);
           
            
            if(isInside(K) && visited[pos][K] == true){
                break;
            }
            
            
            
            
            
            
        }
        
        
        
        
        
        
    }
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      K = sc.nextInt(); 
      
      visited = new boolean[2][500010];
      find = true; 
      
      time = 0; 
        
      if(N != K){
         BFS(N);
      }
      
      if(find == false){
          time = -1; 
      }  
      
        
      System.out.println(time); 
      
      
      
      
    }
}
