import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Lottos {
	
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        Map<Integer, Integer> result = new HashMap<Integer, Integer>();
        result.put(6,1);
        result.put(5,2);
        result.put(4,3);
        result.put(3,4);
        result.put(2,5);
        
        Arrays.sort(lottos);
        Arrays.sort(win_nums);
        
        int zero = 0;
        int com = 0;
        for(int i=0;i<lottos.length;i++) {
        	if(lottos[i] == 0) {
        		zero++;
        	}else {
        		for(int j=0;j<win_nums.length;j++) {
        			if(lottos[i] == win_nums[j]) {
        				com++;
        				break;
        			}
        		}
        	}
        }
        //최고, 최저
        if(zero+com > 1) {
        	answer[0] = result.get(zero+com);
        }else{
        	answer[0] = 6;
        }
        
        if(com > 1) {
        	answer[1] = result.get(com);
        }else {
        	answer[1] = 6;
        }
        
        return answer;
    }
}

//교집합 -> size 
//0의 갯수 -> size 최저, 0 갯수 + 최대

