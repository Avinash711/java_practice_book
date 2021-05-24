class Operation{
    int square(int n){
        return n*n;
    }
}

class Aggregate{
    Operation op = new Operation();
    double pi = 3.14;
    double area(int n){
        return pi* op.square(2);
    }


    public static void main(String[] args){
        Aggregate cir = new Aggregate();
        int radius = 2;
        double result = cir.area(radius);
        System.out.println("Area of circle is : [" + result+"]");
    }

    
}
