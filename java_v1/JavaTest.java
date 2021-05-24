import java.util.ArrayList;
import java.util.HashMap;
public class JavaTest {
    ArrayList<Integer> arr = new ArrayList<Integer>();
    HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
    public static void main(String[] args){
        JavaTest obj = new JavaTest();
        for(int i=0; i < 10; i++ ){
            obj.arr.add(i);
            obj.hash.put(i, i+10);

        }
        System.out.println("Data is: "+ obj.arr + "\nHash: "+ obj.hash);

    }

    
}
