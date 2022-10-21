import java.util.*; 

public class Main {
    
    public static int[] arr;
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      arr = new int[20];
      int sum = 0; 
      int gap = 0; 
      int pos1 = 0;
      int pos2 = 0; 
      
      for(int i=0; i<9; i++){
          arr[i] = sc.nextInt();
          sum += arr[i];
      }
      
      
      Arrays.sort(arr, 0, 9);
      
      gap = sum - 100; 
      
      
      for(int i=0; i<9; i++){
          for(int j=0; j<9; j++){
              if(i != j && (arr[i] + arr[j]  == gap)){
                  pos1 = i;
                  pos2 = j; 
              }
          }
      }
      
      
      for(int i=0; i<9; i++){
          if(i == pos1 || i == pos2){
              continue;
          }else{
              System.out.println(arr[i]);
          }
      }
      
      
      
    }
}
