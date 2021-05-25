import java.util.HashMap;
import java.sql.Array;
import java.util.ArrayList;

public class Duplicate{

    HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();
    public Duplicate(ArrayList<Integer> data_s){
        ArrayList<Integer> numbers = new ArrayList<>();
        numbers = data_s;
        System.out.println(numbers + " "+numbers.size());
        for (int i=0; i<numbers.size();i++){
            if (result.containsKey(numbers.get(i))){
                result.put(numbers.get(i), result.get(numbers.get(i))+1);
                System.out.println(numbers.get(i) + " "+ result);
            }else{
                result.put(numbers.get(i), 1);
                //System.out.println(numbers.get(i) + " "+ result);
            }

        }
        ArrayList<Integer>keys = new ArrayList<>();
        ArrayList<Integer>values = new ArrayList<>();
        for (Integer i: result.keySet()) {
            keys.add(i);
            values.add(result.get(i));
         }
        System.out.println("\nkeys: "+ keys+ " \nvalues :" +values );

        System.out.println("\nResult is:\n");
    }

    public static void main(String[] args){
        ArrayList<Integer> data = new ArrayList<>();
        data.add(1);
        data.add(2);
        data.add(3);
        data.add(2);
        data.add(1);
        data.add(1);
        Duplicate dup = new Duplicate(data);
        System.out.println(dup.result);
        
    }
}