import java.util.*; 

public class Main {
    
    public static int[] arr;
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in); 
      String str = sc.next();
      arr = new int[30];
      StringBuilder sb = new StringBuilder(); 
      
      for(int i=0; i<str.length(); i++){
          int pos = str.charAt(i) - 'A';
          arr[pos] += 1;
      }
      
      int oddCnt = 0; 
      
      for(int i=0; i<=25; i++){
          if(arr[i] % 2 == 1){
              oddCnt += 1;
          }
      }
      
      
      if(oddCnt >= 2){
          System.out.println("I\'m Sorry Hansoo");
          return; 
      }else{
          
          for(int i=0; i<=25; i++){
              if(arr[i] % 2 == 1){
                  sb.append((char)(i+'A'));
                  arr[i] -= 1;
              }
          }
          
          
          for(int i=25; i>=0; i--){
              
              if(arr[i] >= 2){
                  int cnt = arr[i];
                  
                  for(int j=0; j<(cnt/2); j++){
                      sb.insert(0, (char)(i+'A'));
                  }
                  
                  
                  for(int j=0; j<(cnt/2); j++){
                      sb.append((char)(i+'A'));
                  }
                  
              }
              
          }
          
          
          
          System.out.println(sb.toString()); 
          
          
          
          
          
          
      }
      
      
      
      
      
      
      
    }
}
