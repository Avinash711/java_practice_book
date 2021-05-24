public class OverloadMain {
    public  static void main(){
        System.out.println("Main without arguments\n");

    }
    public static void main(String[] args){
        System.out.println("Main jvm loader");
        OverloadMain obj = new OverloadMain();
        obj.main();
    }
    
}
