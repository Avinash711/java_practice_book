class Animal{
    String name = "Animal Data";
    String class_type = "Animal";
    void name(){
        System.out.println("Parent Animal class");
    }
}
class Dog extends Animal{
    String typeAnimal = "Dog";
    String safe = "Friendly";
    String class_type = "Doggg";
    void barking(){
        System.out.println("Dog barks ");
    }
    void display(){
        System.out.println("From Dog:: "+ new Dog().class_type+ " is a: "+ super.class_type);
    }

}


public class Inheritance {
    public static void main(String[] args){
        Dog dog = new Dog();
        dog.barking();
        dog.name();
        System.out.println("Properties:" + dog.name+ " "+ dog.typeAnimal+" "+dog.safe);
        new Dog().display();
        
    }

    
}
