import java.util.*; 

public class Main {
    
    public static int N;
    public static int M; 
    public static char[][] map; 
    public static boolean find;
    public static int jx;
    public static int jy;
    public static int bx;
    public static int by; 
    public static boolean[][] visited; 
    
    public static boolean isInside(int x, int y){
        if(0<=x && x<N && 0<=y && y<M){
            return true;
        }else{
            return false; 
        }
    }
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1}; 
    
    
    public static void DFS(int x, int y){
        
        
          visited[x][y] = true; 
        
          if(map[x][y] == '#'){
              find = true;
              return; 
          }
          
          // System.out.println("x, y, map[x][y]는?" + x + " " + y + " " + map[x][y]);
        
        
          if(map[x][y] == '1'){
              map[x][y] = '*';
              return;
          }else if(map[x][y] == '0'){
              map[x][y] = '*';
          }
          
          
          
          for(int i=0; i<4; i++){
              int nx = x + dx[i];
              int ny = y + dy[i];
              
              if(!isInside(nx,ny)){
                  continue;
              }
              
              if( visited[nx][ny] == false && (map[nx][ny] == '0' || map[nx][ny] == '1' || map[nx][ny] == '#')){
                  DFS(nx,ny); 
              }
          }
        
        
        
        
    }
    
    
    public static void print(){
        
        System.out.println("출력");
        
        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                System.out.print(map[i][j]+ " ");
            }
            System.out.println(); 
        }
    }
    
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt(); 
      M = sc.nextInt(); 
      jx = sc.nextInt();
      jy = sc.nextInt();
      bx = sc.nextInt();
      by = sc.nextInt(); 
      
      map = new char[N+10][M+10];
      
      
      for(int i=0; i<N; i++){
          
          String str = sc.next(); 
          
          for(int j=0; j<M; j++){
              map[i][j] = str.charAt(j);
          }
      }
      
      
      int jump = 0; 
      find = false; 
      
      
      // print(); 
      
      while(true){
          
          
          // System.out.println("현재 점프는?");
          
          jump++; 
          
          visited = new boolean[N+10][M+10];
         
              for(int i=0; i<N; i++){
                  for(int j=0; j<M; j++){
                      if(map[i][j] == '*' && visited[i][j] == false){
                          DFS(i,j);
                          // print();
                      }
                  }
              }
              
              
              if(find == true){
                  break; 
              }
              

          
          
          
          
          
          // print(); 
          // System.out.println("jump는?" + jump);
          // System.out.println("find는?" + find); 
          
          
          
          
      }
      
      
      
      
      
      
      
      System.out.println(jump);
      
      
      
      
      
      
    }
}
