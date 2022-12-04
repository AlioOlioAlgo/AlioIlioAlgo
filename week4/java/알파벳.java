import java.util.*; 

public class Main {
    
    
    public static int R;
    public static int C; 
    public static int maxLength; 
    public static String str; 
    public static boolean[][] visited; 
    public static char[][] map; 
    
    
    
    
    public static boolean isInside(int x, int y){
        if(1<=x && x<=R && 1<=y && y<=C){
            return true;
        }else{
            return false; 
        }
    }
    
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1}; 
    
    public static void DFS(int x, int y){
        
        
        maxLength = Math.max(maxLength, str.length());
        // System.out.println("str은?" + str); 
        
        
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(!isInside(nx,ny)){
                continue;
            }
            
            char c = map[nx][ny]; 
            
            if(!str.contains(Character.toString(c))){
                str += c;
                DFS(nx,ny); 
                str = str.substring(0, str.length()-1);
            }
        }
        
        
        
    }
    
    
  
    
    
    public static void main(String args[]) {
      
         Scanner sc = new Scanner(System.in);
    
         R = sc.nextInt();
         C = sc.nextInt(); 
        
         map = new char[R+10][C+10];
        
         
         maxLength = Integer.MIN_VALUE; 
         str = ""; 
         


         for(int i=1; i<=R; i++){
             String input = sc.next(); 
             // System.out.println("input은?" + input); 
             
             for(int j=1; j<=C; j++){
                 map[i][j] = input.charAt(j-1);
             }
         } 
         
         str += map[1][1];
         // System.out.println("str은?" + str); 
         
         DFS(1, 1);
         
      
         System.out.println(maxLength); 
      
      
      
      
    }
}
