
import java.util.*;

public class ConvertArraySet {

    public static void main(String[] args) {

        char[] array = {"a", "b", "c", "a"};
        Set<Character> set = new HashSet<Character>(Arrays.asList(array));

        System.out.println("Set: " + set);

    }
}