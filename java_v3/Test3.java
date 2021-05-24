/* Insatnce initilizer block demo */
class Demo{
    int speed = 0;
    Demo(){
        System.out.println("Speed is: "+ speed);
    }
    {speed = 100;}

}
public class Test3 {
    public static void main(String[] args){
        Demo demo = new Demo();

    }
   

    
}
