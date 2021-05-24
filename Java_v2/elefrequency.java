class Elefrequency{
    public static void main(String args[]){

        int[] arr = new int[]{1,2,3,1,1,2,2};
        int[] fr = new int[arr.length];
        
        int visited = -1;
        for(int i = 0; i<arr.length; i++){
            int count = 1;
            for (int j = i+1; j<arr.length; j++){
                if (arr[i] == arr[j]){
                    count += 1;
                    fr[j] = visited;
                }

            }
            if (fr[i] != visited){
                fr[i] = count;
            }
        }
        for (int k=0; k<fr.length;k++){
            System.out.print(" "+fr[k]);
        }
        System.out.println("");
        //Displays the frequency of each element present in array  
        System.out.println("---------------------------------------");  
        System.out.println(" Element | Frequency");  
        System.out.println("---------------------------------------");  
        for(int i = 0; i < fr.length; i++){  
            if(fr[i] != visited)  
                System.out.println("    " + arr[i] + "    |    " + fr[i]);  
        }  
        System.out.println("----------------------------------------");  
    }
    
}
