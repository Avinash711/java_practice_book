/** Demo of Runtime polymorphism **/
class Bike{
    int speed;
    Bike(int speed){
        this.speed = speed;
    }
    void run(){
        System.out.println("Bike is having speed");
    }
}

class Jawa extends Bike{
    String model = "JAWA 42.2.1";
    Jawa(int speed){
        super(speed);
        System.out.println("Jawa Constructor:"+ speed);
    }
    void run(){
        super.run();
        System.out.println("Speed: "+ speed+ " model: "+model);

    }
}
public class Test5 {
    public static void main(String[] args){
        Bike ja = new Jawa(500);//upcasting
        ja.run();

    }
    
}
