import java.util.Arrays;
import java.util.HashSet;

public class TwoAdd {
	
    public int[] solution(int[] numbers) {
     
        HashSet<Integer> hs = new HashSet<Integer>();
        
        for(int i=0;i<numbers.length;i++) {
        	for(int j=i+1;j<numbers.length;j++) {
        		hs.add(numbers[i]+numbers[j]);
        	}
        }
        
        int[] answer = new int[hs.size()];
        int n = 0;
        for(int hsNum : hs) {
        	answer[n] = hsNum;
        	n++;
        }
        Arrays.sort(answer);
        
        return answer;
    }
}
