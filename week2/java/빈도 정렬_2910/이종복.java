import java.util.*; 


class Pair implements Comparable<Pair>{
    
    int x;
    int y;
    int order; 
    
    
    public Pair(int x, int y, int order){
        this.x = x;
        this.y = y;
        this.order = order; 
    }
    
    @Override
    public int compareTo(Pair cmp){
        if(this.y == cmp.y){
            return this.order - cmp.order;
        }
        return cmp.y - this.y; 
    }
    
    
    
    
    
}



public class Main {
    public static void main(String args[]) {
     
       Scanner sc = new Scanner(System.in);
       HashMap<Integer, Integer> map = new HashMap<>(); 
       HashMap<Integer, Integer> orderMap = new HashMap<>();
     
       int N = sc.nextInt();
       int C = sc.nextInt();
       ArrayList<Pair> arr = new ArrayList<>();
       
       for(int i=1; i<=N; i++){
           int num = sc.nextInt();
           if(map.containsKey(num)){
               map.put(num, map.get(num)+1);
           }else{
               map.put(num, 1);
               orderMap.put(num, i);
           }
       }
       
       for(Integer num: map.keySet()){
           arr.add(new Pair(num, map.get(num), orderMap.get(num)));
       }
       
       
       
       Collections.sort(arr);
       
       for(int i=0; i<arr.size(); i++){
           int cnt = arr.get(i).y;
           
           for(int j=0; j<cnt; j++){
               System.out.print(arr.get(i).x+ " ");
           }
       }    
     
     
     
    }
}
