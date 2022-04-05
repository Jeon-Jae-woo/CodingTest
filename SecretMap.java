
public class SecretMap {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        String binary1;
        String binary2;
        for(int i=0;i<n;i++) {
        	answer[i] = "";
        	binary1 = Integer.toBinaryString(arr1[i]);
        	binary2 = Integer.toBinaryString(arr2[i]);
        	
        	binary1 = binaryNcode(binary1, n-binary1.length());
        	binary2 = binaryNcode(binary2, n-binary2.length());
        	
        	for(int j=0;j<n;j++) {
        		if(binary1.charAt(j) == '1' || binary2.charAt(j) == '1') {
        			answer[i] += "#";
        		}else{
        			answer[i] += " ";
        		}
        	}    	
        }
        return answer;
    }
    
    public String binaryNcode(String bn, int len) {	
    	String temp = "";
    	for(int i=0;i<len;i++) {
    		temp += "0";
    	}
    	bn = temp + bn;
    	return bn;
    }

}
