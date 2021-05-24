interface Printable{
    void draw();
}
interface Drawable{
    void show();
}
public class InterfaceClass implements Printable, Drawable {
    public void draw(){
        System.out.println("Draw of interface Printable got overridden");
    }
    public void show(){
        System.out.println("show of interface Drawable got overridden");
    }
    public static void main(String[] args){
        InterfaceClass inter = new InterfaceClass();
        inter.draw();
        inter.show();


    }
    
}
