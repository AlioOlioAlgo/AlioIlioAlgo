import java.util.*; 




class Info{
    
    int x1;
    int y1;
    int x2;
    int y2; 
    
    
    public Info(int x1, int y1, int x2, int y2){
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2; 
    }
}





public class Main {
    
    public static int N;
    public static int M; 
    public static int[][] info; 
    public static int[][] map;
    public static boolean[][][][] wall; 
    public static boolean[][] visited; 
    public static int cnt; 
    
    
    public static int[] dx = {0, -1, 0, 1};
    public static int[] dy = {-1, 0, 1, 0};
    
    
    public static boolean isInside(int x, int y){
        if(0<=x && x<M && 0<=y && y<N){
            return true;
        }else{
            return false; 
        }
    }
    
    
    public static int[] calculate(int num){
        
        int[] tmp = new int[4];
        
        int pos = 0;
        
        while(num != 0){
            
            int remain = num % 2;
            tmp[pos++] = remain;
            num /= 2;
        }
        
        return tmp; 
        
    }
    
    
    public static void DFS(int x, int y){
        
        visited[x][y] = true;
        cnt++; 
        
        
        for(int i=0; i<4; i++){
            
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(!isInside(nx,ny)){
                continue;
            }
            
            if(visited[nx][ny] == false && wall[x][y][nx][ny] == false){
                // System.out.println("x, y에서 nx,ny로 이동" + x + " " + y + " " + nx + " " + ny);
                DFS(nx, ny);
            }
            
            
        }
        
        
        
        
    }
    
    
    
    
    
    public static void main(String args[]) {
        
      Scanner sc = new Scanner(System.in);
      
      N = sc.nextInt();
      M = sc.nextInt(); 
      info = new int[M+10][N+10];  
      map = new int[M+10][N+10];
      wall = new boolean[M+10][N+10][M+10][N+10];
      visited = new boolean[M+10][N+10];
      int maxCnt = Integer.MIN_VALUE; 
      int maxdeleteCnt = Integer.MIN_VALUE; 
      
      ArrayList<Info> arr = new ArrayList<>(); 
      
      int rooms = 0; 
      
      for(int i=0; i<M; i++){
          for(int j=0; j<N; j++){
              info[i][j] = sc.nextInt();
              map[i][j] = 0; 
          }
      }        
      
      
      for(int i=0; i<M; i++){
          for(int j=0; j<N; j++){
              int num = info[i][j];
              
              int[] res = calculate(num);
              
              for(int k=0; k<4; k++){
                  
                  int nx = i + dx[k];
                  int ny = j + dy[k];
                  
                  if(!isInside(nx,ny)){
                      continue;
                  }
                  
                  // System.out.println("k, res[k]는?" + k + " " + res[k]);
                  
                  if(res[k] == 1){
                      // System.out.println("진입!");
                      // System.out.println("i, j, nx, ny는?" + i + " " + j + " " + nx + " " +ny);
                      wall[i][j][nx][ny] = true;
                      arr.add(new Info(i, j, nx, ny));
                      wall[nx][ny][i][j] = true; 
                  }
              }
          }
      }
      
      
      
      for(int i=0; i<M; i++){
          for(int j=0; j<N; j++){
              if(visited[i][j] == false){
                  // System.out.println("i, j진입" + i + " " + j);
                  rooms++;
                  cnt = 0; 
                  DFS(i, j);
                  maxCnt = Math.max(maxCnt, cnt); 
                  
              }
          }
      }
      
      System.out.println(rooms);
      System.out.println(maxCnt);
      
      
      for(int i=0; i<arr.size(); i++){
          
          visited = new boolean[M+10][N+10];
          
          int x1 = arr.get(i).x1;
          int y1 = arr.get(i).y1;
          int x2 = arr.get(i).x2;
          int y2 = arr.get(i).y2; 
          
          wall[x1][y1][x2][y2] = false;
          wall[x2][y2][x1][y1] = false;
          
         for(int j=0; j<M; j++){
          for(int k=0; k<N; k++){
              if(visited[j][k] == false){
                  cnt = 0; 
                  DFS(j, k);
                  // System.out.println("i, cnt는?" + i + " " + cnt);
                  maxdeleteCnt = Math.max(maxdeleteCnt, cnt); 
                  
              }
          }
        }
          
          
          wall[x1][y1][x2][y2] = true;
          wall[x2][y2][x1][y1] = true;
          
      }
      
      
      System.out.println(maxdeleteCnt); 
      
      
      
        
        
        
        
        
        
        
    }
}
