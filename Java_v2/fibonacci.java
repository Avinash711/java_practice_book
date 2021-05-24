class fibonacci{
    
    public static void main(String args[]){
        int n1 = 0,n2=1,num=10, ind;
        int n3;
        System.out.print(n1 + " " + n2);

        for(ind = 0; ind <= num ; ind++){
            n3 = n1 + n2;
            n1 = n2;
            n2 = n3;
            System.out.print(" " + n2);

        }

    }
    
}
