import java.util.Arrays;

public class MinValue {
	//�ּҰ� �����
    public int solution(int []A, int []B){
        int answer = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        int bLen = B.length-1;
        
        for(int i=0;i<A.length;i++) {
        	answer += (A[i] * B[bLen]);
        	bLen--;
        }

        return answer;
    }
}
