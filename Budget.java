import java.util.Arrays;

public class Budget {
	
    public int solution(int[] d, int budget) {
        Arrays.sort(d);
        int count = 0;
        int index = 0;
        while(budget > 0) {
        	budget -= d[index];
        	if(budget < 0) {
        		break;
        	}
        	
        	count++;
        	index++;
        	if(index >= d.length) {
        		break;
        	}
        }
        return count;
    }
}
