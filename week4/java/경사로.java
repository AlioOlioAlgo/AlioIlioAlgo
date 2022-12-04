import java.util.*; 

public class Main {
    
    public static int N;
    public static int L;
    public static int[][] map;
    public static int[][] tmpMap; 
    public static boolean[][] check; 
    
    public static boolean checkRows(int row){
        
        
         
         for(int i=0; i<N; i++){
             if(map[row][i] == map[row][i+1]){
                 continue;
             }else{
                 
                 int gap = map[row][i+1]-map[row][i];
                 
                 if(gap == 1){
                     
                     int curr = i;
                     int len = L;
                     
                     
                     while(len != 0){
                         
                         if(0<=curr && curr < N && check[row][curr] == false){
                            check[row][curr] = true;
                            curr--;
                         }else{
                             return false; 
                         }
                         len--; 
                         
                     }
                 }else if(gap >= 2){
                     return false;
                 }
                 
                 
                 
             }
             
         }
        
        
         for(int i=N-1; i>=1; i--){
             if(map[row][i] == map[row][i-1]){
                 continue;
             }else{
                 
                 int gap = map[row][i-1]-map[row][i];
                 
                 if(gap == 1){
                     
                     int curr = i;
                     int len = L;
                     
                     
                     while(len != 0){
                         
                         if(0<=curr && curr < N && check[row][curr] == false){
                            check[row][curr] = true;
                            curr++;
                         }else{
                             return false; 
                         }
                         len--; 
                         
                     }
                 }else if(gap >= 2){
                     return false;
                 }
                 
                 
                 
             }
             
         }
        
        
        
         return true; 
        
        
        
    }
    
    
    
    
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      int answer = 0; 
      
      N = sc.nextInt();
      L = sc.nextInt(); 
      
      map = new int[110][110];
      tmpMap = new int[110][110];
      check = new boolean[110][110]; 
      
      for(int i=0; i<N; i++){
          for(int j=0; j<N; j++){
              map[i][j] = sc.nextInt();
          }
      }
      
      for(int i=0; i<N; i++){
          boolean result = checkRows(i); 
          if(result){
              // System.out.println("i는?" + i);
              answer++;
          }
      }
      
      
      for(int i=0; i<N; i++){
          for(int j=0; j<N; j++){
              tmpMap[i][j] = map[j][i];
          }
      }
      
      
      
      for(int i=0; i<N; i++){
          for(int j=0; j<N; j++){
              map[i][j] = tmpMap[i][j];
          }
      }
      
      /*
      for(int i=0; i<N; i++){
          for(int j=0; j<N; j++){
              System.out.print(map[i][j]+ " ");
          }
          System.out.println(); 
      }
      */
      
      check = new boolean[110][110];
      
      for(int i=0; i<N; i++){
          boolean result = checkRows(i); 
          if(result){
              // System.out.println("i는?" + i);
              answer++;
          }
      }
      
      
      
      
      System.out.println(answer); 
      
      
      
    }
}
