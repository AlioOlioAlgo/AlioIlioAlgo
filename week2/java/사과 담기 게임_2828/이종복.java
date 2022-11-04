import java.util.*; 

public class Main {
    
    
    
    
    
    
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in);
      
      int N = sc.nextInt();
      int M = sc.nextInt();
      int j = sc.nextInt(); 
      
      
      int start = 1;
      int end = M;
      int distance = 0; 
      
      
      for(int i=1; i<=j; i++){
          
          int pos = sc.nextInt(); 
          
          if(start<=pos && pos<=end){
              continue;
          }else if(end < pos){
              int gap = pos-end;
              distance += gap;
              start += gap;
              end += gap;
          }else if(pos < start){
              int gap = start-pos;
              distance += gap;
              start -= gap;
              end -= gap;
          }
          
          
          
      }
      
      System.out.println(distance); 
      
      
      
      
      
      
    }
}
