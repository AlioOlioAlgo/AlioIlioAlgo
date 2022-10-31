import java.util.*; 

public class Main {
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in); 
      
      int N = sc.nextInt();
      
      int cnt = 0;
      int num = 1; 
      
      while(true){
          
          String str = Integer.toString(num);
          
          int len = str.length();
          
          boolean isTrue = false;
          
          int sixSequence = 0;
          
          for(int i=0; i<len; i++){
              char c = str.charAt(i);
              
              if(c == '6'){
                  sixSequence++;
              }else{
                  sixSequence = 0; 
              }
              
              
              if(sixSequence == 3){
                isTrue = true;
                break;
              }
          }
          
          
          if(isTrue){
              cnt++;
          }
          
          if(cnt == N){
              break;
          }else{
              num++;
          }
      }
      
      System.out.println(num); 
      
      
      
    }
}
