import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Main T = new Main();
      
      Scanner sc = new Scanner(System.in);
      
      int H = sc.nextInt();
      int W = sc.nextInt();
      
      char[][] map = new char[H+10][W+10];
      int[][] result = new int[H+10][W+10];
      
      for(int i=0; i<H; i++){
          String str = sc.next(); 
          
          for(int j=0; j<W; j++){
              map[i][j] = str.charAt(j);   
          }
      }
      
      
      for(int i=0; i<H; i++){
          for(int j=0; j<W; j++){
              result[i][j] = -1;
          }
      }
      
      
      for(int i=0; i<H; i++){
          
          boolean cExist = false;
          int num = 1;
          
          for(int j=0; j<W; j++){
              
              if(map[i][j] == 'c'){
                  result[i][j] = 0;
                  cExist = true;
                  num = 1;
              }else if(cExist == true){
                  result[i][j] = num;
                  num++;
              }else if(cExist == false){
                  continue; 
              }
              
          }
      }
      
      for(int i=0; i<H; i++){
          for(int j=0; j<W; j++){
              System.out.print(result[i][j]+ " ");
          }
          System.out.println(); 
      }
      
      
      
      
      
      
      
      
      
      
    }
}
