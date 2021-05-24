
/* user input form array
*/
import java.util.Scanner;
import java.util.ArrayList;

class Demo{
    ArrayList<String> arr = new ArrayList<String>();
    Demo(){
        System.out.println("Demo Default constructor");
    }
    Demo(ArrayList<String> arr){
        this.arr = arr;
    }
    public void display(){
        System.out.print("Array is : "+ arr);
    }
}
class Scan {
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the size of array:");
        int size = sc.nextInt();
        ArrayList<String> arr = new ArrayList<String>();
        for(int i = 0; i <size; i++){
            arr.add(sc.next());
        }
        Demo df = new Demo();
        System.out.println("Type name::::"+ df.getClass().getSimpleName());
        Demo d = new Demo(arr);

        d.display();

    }
    
    
    
}
