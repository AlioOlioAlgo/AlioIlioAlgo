import java.util.*; 

public class Main {
    
    public static int N;
    public static int[][] map;
    public static boolean[][] visited; 
    
    public static int[] dx= {-1, 1, 0, 0};
    public static int[] dy ={0, 0, -1, 1};
    
    public static boolean isInside(int x, int y){
        if(0<=x && x<N && 0<=y && y<N){
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
            
            if(isInside(nx,ny) && visited[nx][ny] == false){
                DFS(nx, ny);
            }
        }
        
        
    }
    
    public static void main(String args[]) {
      
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        map = new int[N+10][N+10];
        int maxArea = Integer.MIN_VALUE;
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                map[i][j] = sc.nextInt();
            }
        }
        
        
        
        for(int i=0; i<=100; i++){
            
            int area = 0; 
            visited = new boolean[N+10][N+10];
            
            for(int j=0; j<N; j++){
                for(int k=0; k<N; k++){
                    if(map[j][k] <= i){
                        visited[j][k] = true;
                    }
                }
            }
            
            
            for(int j=0; j<N; j++){
                for(int k=0; k<N; k++){
                    if(visited[j][k] == false){
                        area++;
                        DFS(j, k);
                    }
                }
            }
            
            
            
            maxArea = Math.max(maxArea, area);
            
            
            
        }
        
        
        System.out.println(maxArea); 
        
        
      
      
      
      
      
    }
}
