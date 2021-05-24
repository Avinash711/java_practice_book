public class arraycopy {

    public static void main(String args[]){
        int[] arr1 = new int[]{1,2,3,4,5,6};
        int[] arr2 = new int[arr1.length];

        for (int i=0; i <arr1.length; i++){
            arr2[i] = arr1[i];

        }

        
        for (int j = 0; j<arr1.length;j++){
            System.out.print(" "+arr1[j]);
           

        }
        System.out.println("");

        for (int j = 0; j<arr2.length;j++){
            System.out.print(" "+arr2[j]);
            
        }
       
    }
    
}
