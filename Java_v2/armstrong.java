public class armstrong {

    static int return_arms(int num){
        int sum = 0, rem;
        while(num > 0){
            rem = num % 10;
            sum = sum +  (rem*rem*rem);
            num = num /10;
            
        }
        return sum;
    }

    public static void main(String args[]){
        int num = 153;
        int result = return_arms(num);
        if (result == num){
            System.out.println(num + " is armstsrong matches with result as : "+ result);
        }
        else{
            System.out.println(num + " is not armstsrong and doesnot matches with result as : "+ result);

        }
    }
    
}
