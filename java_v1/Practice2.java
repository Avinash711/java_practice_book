import java.util.Scanner;
import java.util.Arrays;
class Getter{
    int size;
    String[] arr;
    public void setter(int size, String[] arr){
        this.size = size;
        this.arr = arr;
        System.out.println("Data: " +this.size+ " ::" + Arrays.toString(this.arr) );
    }

    public void display_getter(){
        for (int i = 0; i< this.size; i ++){
            System.out.println("Index: "+ i + " Element: "+ this.arr[i]);
        }
        
    }
}

public class Practice2 {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the size of array: ");
        int size = sc.nextInt();
        String[] array =  {"Java", "Python", "Scala", "C++"};
        Getter obj = new Getter();
        obj.setter(size, array);
        obj.display_getter();

    }

    
}
