import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      String str = sc.nextLine();
      StringBuilder sb = new StringBuilder();
      
      System.out.println(str); 
      if(str.length() == 0){
          System.out.println("");
          return;
      }
      
      for(int i=0; i<str.length(); i++){
          char c = str.charAt(i);
          
          if(65<=c && c<=90){
              int num = c + 13; 
              if(num >= 91){
                  num -= 26;
              }
              
              sb.append((char)num);
          }else if(97<=c && c<=122){
              int num = c + 13; 
              if(num >= 123){
                  num -= 26;
              }
              
              sb.append((char)num);
          }else{
              sb.append(c);
          }
          
      }
      
      System.out.println(sb.toString()); 
      
      
    }
}
