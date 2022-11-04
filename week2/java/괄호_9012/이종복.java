import java.util.*; 

public class Main {
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in);
      
      
      int T = sc.nextInt();
      
      for(int i=1; i<=T; i++){
          
          String str = sc.next();
          
          int len = str.length();
          boolean isTrue = true;
          
          
          Stack<Character> stk = new Stack<>();
          
          for(int j=0; j<len; j++){
              
              char c = str.charAt(j);
              
              if(c == '('){
                  stk.push(c);
              }else{
                  
                  if(stk.size() == 0){
                      System.out.println("NO");
                      isTrue = false;
                      break;
                  }else{
                      
                      if(stk.peek() == ')'){
                          System.out.println("NO");
                          isTrue = false;
                          break;
                      }else{
                          stk.pop();
                      }
                  }
                  
                  
                  
                  
              }
          }
          
          if(isTrue == false){
              continue;
          }
          
          if(stk.size() == 0){
              System.out.println("YES");
          }else{
              System.out.println("NO");
          }
          
          
          
      }
       
      
      
      
      
    }
}
