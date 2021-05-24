import java.util.ArrayList;
import java.util.Scanner;
class Logic{
    public ArrayList<String> returnArray(ArrayList<String> arr){
        for(int i=0; i<arr.size(); i++){
            arr.set(i, arr.get(i)+" Known");
        }
        return arr ;
    }
}
public class ReturnArrayClass {
    public static void main(String[] args){
        ArrayList<String> arr = new ArrayList<>();
        arr.add("Python");
        arr.add("Java");
        arr.add("C++");
        arr.add("Scala");
        System.out.println("Array arr is :"+ arr);
        ArrayList<String> copy_arr  = new ArrayList<>(arr);
        System.out.println("Copied arr: "+ copy_arr);
        Logic obj = new Logic();
       
        
        ArrayList<String> ret = obj.returnArray(arr);
        System.out.println(ret);

    }
    
}
