import java.util.Scanner;
import java.util.Arrays;
public class Practice {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the size of array:");

        int size = sc.nextInt();
        String[] array = new String[size];
        System.out.println("\nEnter the elements:");

        for (int i = 0; i< size; i++){
            array[i] = sc.next();
        }
        System.out.println("\nThe elements are:" +  Arrays.toString(array));
        System.out.println("\nThe elements are:" +  Arrays.asList(array));

        for (int i = 0; i < array.length; i++){
            System.out.println("\nIndex: " + i + " Element is: "+ array[i] + ", type : "+ 
                                array[i].getClass().getSimpleName());
        }
    }
    
}
