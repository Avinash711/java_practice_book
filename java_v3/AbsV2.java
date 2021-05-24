abstract class Shape{
    abstract void draw();
}
class Rectangle extends Shape{
    void draw(){
        System.out.println("Draw of Rectangle");
    }
}
class Square extends Shape{
    void draw(){
        System.out.println("Draw of Square");
    }
}

public class AbsV2 {
    public static void main(String[] args){
        Shape s;
        s = new Rectangle();
        s.draw();
        s = new Square();
        s.draw();
    }
    
}
