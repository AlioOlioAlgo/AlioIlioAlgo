import java.util.*; 


class Pair{
    int x; 
    int y;
    
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}



public class Main {
    
    public static int R;
    public static int C; 
    public static char[][] map;
    public static boolean[][] visited; 
    public static Queue<Pair> water;
    public static Queue<Pair> q;
    public static Pair[] swans; 
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};
    
    public static boolean isInside(int x, int y){
        if(0<=x && x<R && 0<=y && y<C){
            return true;
        }else{
            return false;
        }
    }
    
    
    public static void main(String args[]) {
    
    
      Scanner sc = new Scanner(System.in);
      
      R = sc.nextInt();
      C = sc.nextInt();
      
      map = new char[R+10][C+10];
      visited = new boolean[R+10][C+10];
      swans = new Pair[2];
      water = new LinkedList<>(); 
      q = new LinkedList<>(); 
      
      int swanCnt = 0; 
      
      for(int i=0; i<R; i++){
          
          String str = sc.next();
          
          for(int j=0; j<C; j++){
              map[i][j] = str.charAt(j);
          }
      }
      
      
      for(int i=0; i<R; i++){
          for(int j=0; j<C; j++){
               if(map[i][j] == 'L'){
                   swans[swanCnt++] = new Pair(i, j);
               }
               
               if(map[i][j] != 'X'){
                   water.add(new Pair(i,j));
               }
          }
      }
      
      q.add(swans[0]);
      visited[swans[0].x][swans[0].y] = true;
      boolean meet = false;         
      int days = 0;     
        
      while(true){
          
          Queue<Pair> nextQ = new LinkedList<>(); 
          
          
          while(!q.isEmpty()){
              
              Pair curr = q.poll();
              int x = curr.x;
              int y = curr.y; 
              if(x == swans[1].x && y == swans[1].y){
                  meet = true;
                  break; 
              }
              
              
              for(int i=0; i<4; i++){
                  
                  int nx = x + dx[i];
                  int ny = y + dy[i];
                  
                  if(!isInside(nx,ny) || visited[nx][ny]){
                      continue;
                  }
                  
                  
                  visited[nx][ny] = true;
                  
                  if(map[nx][ny] == 'X'){
                      nextQ.add(new Pair(nx,ny));
                      continue;
                  }
                  
                  q.add(new Pair(nx,ny));
                  
              }
          }
          
          if(meet){
              break;
          }
          
          q = nextQ; 
          
          
          int len = water.size(); 
          
          
          
          for(int i=0; i<len; i++){
           
             Pair curr = water.poll(); 
             int x = curr.x;
             int y = curr.y; 
           
             for(int j=0; j<4; j++){
                 
                 int nx = x + dx[j];
                 int ny = y + dy[j];
                 
                 if(!isInside(nx,ny)){
                     continue;
                 }
                 
                 if(map[nx][ny] == 'X'){
                     map[nx][ny] = '.';
                     water.add(new Pair(nx,ny));
                 }
                 
             }  
           
              
          }
          
          
          
          
          days++; 
          
          
          
          
          
          
          
          
      }
      
      
      
      
      
      System.out.println(days); 
      
      
      
      
      
      
      
      
      
    }
}
