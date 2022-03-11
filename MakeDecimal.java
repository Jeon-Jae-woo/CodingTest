import java.util.ArrayList;

public class MakeDecimal {

    public int solution(int[] nums) {
        int answer = 0;
      
        ArrayList<Integer> hashNum = new ArrayList<Integer>();
      
        for(int i=0;i<nums.length;i++) {
        	for(int j=i+1;j<nums.length;j++) {
        		for(int z=j+1;z<nums.length;z++) {
        			hashNum.add(nums[i]+nums[j]+nums[z]);
        		}
        	}
        }
        
        for(Integer i : hashNum) {
        	boolean check = Decimal(i);
        	if(check) {
        		answer++;
        	}
        }

        return answer;
    }
	
    
    public boolean Decimal(Integer num) {
    	for(int i=2;i<num;i++) {
    		if(num%i==0) {
    			return false;
    		}
    	}
    	return true;
    }
	
}
