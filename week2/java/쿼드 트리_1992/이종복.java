import java.util.*; 

public class Main {
    
    public static int N;
    public static int[][] map;
    
    public static boolean isSame(int sx, int sy, int ex, int ey){
        
        int num = map[sx][sy];
        
        
        boolean allSame = true;
        
        for(int i=sx; i<ex; i++){
            for(int j=sy; j<ey; j++){
                if(map[i][j] != num){
                    allSame = false;
                }
                
            }
        }
        
        
        return allSame;
        
    }
    
    
    public static String DFS(int sx, int sy, int ex, int ey, int N){
        
        if(N == 1){
            return Integer.toString(map[sx][sy]);
        }
        
        
        boolean result = isSame(sx, sy, ex, ey);
        
        
        if(result == true){
            return Integer.toString(map[sx][sy]);
        }else{
            
            String str1 = DFS(sx, sy, sx+(N/2), sy+(N/2), (N/2));
            String str2 = DFS(sx, sy+(N/2), sx+(N/2), sy+N, (N/2));
            String str3 = DFS(sx+(N/2), sy, sx+N, sy+(N/2), (N/2));
            String str4 = DFS(sx+(N/2), sy+(N/2), sx+N, sy+N, (N/2));
            
            return '(' + str1+str2+str3+str4 + ')'; 
            
        }
        
        
        
        
        
        
    }
    
    
    
    
    
    
    
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      
      map = new int[N+10][N+10];
      
      
      for(int i=0; i<N; i++){
          String str = sc.next();
          
          for(int j=0; j<N; j++){
              map[i][j] = str.charAt(j)-'0';
          }
      }
     
      
      String result = DFS(0, 0, N, N, N);
      
      
      System.out.println(result);
      
      
      
      
      
      
      
      
      
      
      
    }
}
