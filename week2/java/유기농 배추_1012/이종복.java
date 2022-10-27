import java.util.*; 

public class Main {
    
    
    public static int[][] map;
    public static boolean[][] visited; 
    public static int N;
    public static int M; 
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    
    public static boolean isInside(int x, int y){
        if(0<=x && x<N && 0<=y && y<M){
            return true;
        }else{
            return false;
        }
    }
    
    
    public static void DFS(int x, int y){
        
        visited[x][y] = true;
        
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(isInside(nx,ny) && visited[nx][ny] == false && map[nx][ny] == 1){
                   DFS(nx ,ny);
            }
        }
        
    }
    
    
    public static void main(String args[]) {
      
      
      Scanner sc = new Scanner(System.in);
      
      int T = sc.nextInt();
      
      for(int i=1; i<=T; i++){
          
          int answer = 0; 
          
          M = sc.nextInt();
          N = sc.nextInt();
          int K = sc.nextInt();
          
          map = new int[N+10][M+10];
          visited = new boolean[N+10][M+10];
          
          
          for(int j=1; j<=K; j++){
              int x = sc.nextInt();
              int y = sc.nextInt();
              map[y][x] = 1;
          }
          
          
          for(int j=0; j<N; j++){
              for(int k=0; k<M; k++){
                  if(map[j][k] == 1 && visited[j][k] == false){
                      answer++;
                      
                      DFS(j, k);
                      
                      
                  }
              }
          }
          
          
          System.out.println(answer); 
          
          
          
          
      }
      
      
      
      
      
      
    }
}
