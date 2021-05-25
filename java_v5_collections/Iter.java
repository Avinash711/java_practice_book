import java.util.ArrayList;
import java.util.Iterator;
public class Iter {
    public static void main(String[] args){
        ArrayList<String> arr = new ArrayList<>();
        arr.add("Python");
        arr.add("Java");
        arr.add("C++");
        arr.add("Scala");

        Iterator itr = arr.iterator();
        while(itr.hasNext()){
            System.out.println("Element is: "+ itr.next());
        }

    }
    
}
