import java.util.*; 

public class Main {
    
    public static long C; 
    
    public static long recursive(long A, long exponent){
        
        if(exponent == 1){
            return A % C;
        }
        
        
        long temp = recursive(A, exponent/2);
        
        
        if(exponent % 2 == 1){
            return (temp * temp % C) * A % C;
        }
        
        
        return temp*temp % C;
        
    }
    
    
    
    public static void main(String args[]) {
      
      Scanner sc = new Scanner(System.in);
      
      long A = sc.nextLong();
      long B = sc.nextLong();
      
      C = sc.nextLong();
      
      long result = recursive(A, B);
      
      System.out.println(result); 
      
      
      
    }
}
