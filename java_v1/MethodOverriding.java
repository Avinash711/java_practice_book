/* Q: can we acheive method overriding by just changing 
  the return type of method ? */

/* Ans:: */
class A{
    A get(){
        System.out.println("Class A");
        return this;}
}
class B extends A{
    B get(){
        System.out.println("Class B");
        return this;}
}
public class MethodOverriding {
    public static void main(String[] args){
        System.out.println("Covariant return type");
        new B().get();
    }

    
}
