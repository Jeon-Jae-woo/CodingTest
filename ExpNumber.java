
public class ExpNumber {
	
    public int solution(int n) {
        int answer = 0;
        
        //모든 조합 경우의 수
        int sum;
        for(int i=1;i<=n;i++) {
        	sum = 0;
        	for(int j=i;j<=n;j++) {
        		sum += j;
        		if(sum == n) {
        			answer++;
        			break;
        		}
        		if(sum > n) {
        			break;
        		}
        	}
        }
        
        return answer;
    }
}
