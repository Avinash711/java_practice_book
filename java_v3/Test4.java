/**  can we intililize final variable?
    Ans: Yes, only inside consutructor **/

class Demo{
    final int speed; //blank final variable
    static String name = "Ducati";
    Demo(int speed){
        this.speed = speed;
    }

}
public class Test4 {
    public static void main(String[] args){
        Demo demo = new Demo(5000);
        System.out.println(demo.speed);
        System.out.println(Demo.name);
    }
    
}
