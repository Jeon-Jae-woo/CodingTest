
public class AddNumbersEx {
    public int solution(int[] numbers) {
    	// 1 2 3 4 5 6 7 8 9
    	// 45 - numbers[i] 
        int answer = 45;
        
        for(int i=0;i<numbers.length;i++) {
        	answer -= numbers[i];
        }
        return answer;
    }
}
