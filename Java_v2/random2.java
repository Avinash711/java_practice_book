import java.util.Random;

public class random2 {
    public static void main(String args[]){

        Random random = new Random();
        for(int i = 0; i<500;i++){
            i = i + 5;
            int x = random.nextInt(i);
            System.out.print(" " + x);
        }

    }
    
}
