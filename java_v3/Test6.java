/* Data members are not overridden */
class Demo{
    int speedlimit = 100;
}
class Speed extends Demo{
    int speedlimit = 50;
}
public class Test6{
    public static void main(String[] args ){
        Demo d = new Speed();
        System.out.println(d.speedlimit);
        Speed s = new Speed();
        System.out.println(s.speedlimit);
    }
    
}
