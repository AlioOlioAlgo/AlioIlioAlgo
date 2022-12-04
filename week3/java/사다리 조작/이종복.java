import java.util.*; 

public class Main {
    
    public static int[][] line; 
    public static int answer; 
    public static int H;
    public static int N; 
    public static boolean finish; 
    

    
    
    public static boolean check(){
        
        
        boolean isAllSame = true;
        
        
        for(int i=1; i<=N; i++){
            
            int y = i;
            int h = 1;
            
            for(int j=1; j<=H; j++){
                
                if(line[h][y] == 1){
                    y++;
                }else if(line[h][y] == 2){
                    y--;
                }
                h++;
                
            }
            
            if(y != i){
                isAllSame = false;
                break;
            }
        }
        
        
        return isAllSame; 
    
        
    }
    
    
    
    
    public static void DFS(int cnt){
        
         if(finish) return;  
         
         if(answer == cnt){ 
             
             if(check()) finish = true;
             return; 
         }
         
         
         for(int i=1; i<=H; i++){
             for(int j=1; j<=N-1; j++){
                 if(line[i][j] == 0 && line[i][j+1] == 0){
                     line[i][j] = 1;
                     line[i][j+1] = 2;
                     DFS(cnt+1);
                     line[i][j] = 0;
                     line[i][j+1] = 0; 
                 }
                 
             }
         }
         
         
         
        
        
    }
    
    
    
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      int M = sc.nextInt();
      H = sc.nextInt();
      finish = false; 
      
      line = new int[H+10][N+10];
      
      for(int i=1; i<=M; i++){
          
          int a = sc.nextInt();
          int b = sc.nextInt();
          
          line[a][b] = 1;
          line[a][b+1] = 2; 
      }
      
      
      for(int i=0; i<=3; i++){
          answer = i;
          DFS(0);
          if(finish) break;
      }
      
      
       System.out.println((finish) ? answer : -1);
      
      
      
      
      
      
      
    }
}
