import java.util.Arrays;
public class StringClass{
    String name = "Avinash Gaurav";
    public static void main(String[] args){
        StringClass s = new StringClass();
        for (int i=0; i<s.name.length();i++){
            System.out.print(s.name.charAt(i));
        }
        char[] str = s.name.toCharArray();
        System.out.println("\n"+Arrays.toString(str));

    }
}