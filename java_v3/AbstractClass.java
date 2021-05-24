abstract class Vehicle{
    abstract void run();
}
class AbstractClass extends Vehicle {
    void run(){
        System.out.println("Abstract run method override is must");
    }
    public static void main(String[] args){
        AbstractClass ab = new AbstractClass();
        System.out.println("main Method is called");
        ab.run();

    }
    
}
