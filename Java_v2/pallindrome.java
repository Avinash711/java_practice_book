public class pallindrome {

    public static void main(String args[]){
        int num=121;
        int rem, sum=0;
        int temp = num;

        while (num > 0){
            rem = num % 10;
            sum = (sum * 10) + rem;
            num = num /10;

        }
        if (sum == temp){
            System.out.println("Given number is pallindrome!!"+ sum);
        }else{
            System.out.println("Not a pallindrome number!!"+ sum);
        }
    }
    
};
