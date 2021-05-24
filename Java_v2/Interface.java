
interface Drawable{  
    void draw();  
    static int cube(int x){return x*x*x;}  
    default void display(){System.out.println("Default method!!!");}; 
    }  
class Rectangle implements Drawable{  
public void draw(){System.out.println("drawing rectangle");}  
}  
      
class Interface{  
    public static void main(String args[]){  
    Drawable d=new Rectangle();  
    d.draw();  
    d.display();
    System.out.println(Drawable.cube(3));  
}}  