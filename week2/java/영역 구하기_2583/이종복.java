import java.util.*; 

public class Main {
    
    public static int M;
    public static int N;
    public static int K;
    public static boolean[][] visited;
    public static int[][] map;
    public static int cnt; 
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, 1, -1}; 
    
    public static boolean isInside(int x, int y){
        if(0<=x && x<M && 0<=y && y<N){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public static void DFS(int x, int y){
        
        
         visited[x][y] = true;
         cnt++;
         
         
         for(int i=0; i<4; i++){
             int nx = x + dx[i];
             int ny = y + dy[i];
             
             if(isInside(nx,ny) && visited[nx][ny] == false && map[nx][ny] == 0){
                 DFS(nx,ny);
             }
         }
        
        
        
    }
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      M = sc.nextInt();
      N = sc.nextInt();
      K = sc.nextInt();
      
      int area = 0; 
      
      map = new int[M+10][N+10];
      visited = new boolean[M+10][N+10];
      ArrayList<Integer> arr = new ArrayList<>(); 
      
      for(int i=1; i<=K; i++){
          
          int x1 = sc.nextInt();
          int y1 = sc.nextInt();
          int x2 = sc.nextInt();
          int y2 = sc.nextInt();
          
          for(int j=y1; j<y2; j++){
              for(int k=x1; k<x2; k++){
                  map[j][k] = 1;
              }
          }
          
      /*      
      for(int j=0; j<M; j++){
          for(int k=0; k<N; k++){
              System.out.print(map[j][k] + " " );
          }
          System.out.println(); 
      }
      
      System.out.println(); 
        */  
          
      }
      /*
      for(int i=0; i<M; i++){
          for(int j=0; j<N; j++){
              System.out.print(map[i][j] + " " );
          }
          System.out.println(); 
      }
      */
      
      
      for(int i=0; i<M; i++){
          for(int j=0; j<N; j++){
              if(map[i][j] == 0 && visited[i][j] == false){
                  area++;
                  cnt = 0;
                  DFS(i, j);
                  // System.out.println("i, j, cnt는?" + i+  " " + j + " " + cnt);
                  arr.add(cnt); 
              }
          }
      }
      
      
      Collections.sort(arr); 
      
      
      System.out.println(area); 
      
      for(int i=0; i<arr.size(); i++){
          System.out.print(arr.get(i)+ " ");
      }
      
      
      
      
      
      
    }
}
