import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
public class LinkedListCls {
    public static void main(String[] args){
        LinkedList<String> li = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        for(int i=0; i<3;i++){
            li.add(sc.next());
        }
        System.out.println(li);
        Iterator itr = li.iterator();
        while(itr.hasNext()){
            System.out.println(itr.next());
        }
    }

    
}
