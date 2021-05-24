
/* block execution order*/
class Parent{
    Parent(){
        System.out.println("Parent Class constructor is called");
        
    }
    public void method(){
        System.out.println("Parent Class Method is called");
    }
}
public class Test1 extends Parent {
    Test1(){
        super.method();
        System.out.println("Test1 constructor called");

    }
    {System.out.println("Instance Initilizer block");}
    static {System.out.println("Static block");}

    public static void main(String[] args){
        System.out.println("Main method");
        Test1 test = new Test1();
        test.method();
        
    }  
}
