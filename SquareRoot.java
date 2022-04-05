
public class SquareRoot {
    public long solution(long n) {
        //정수 제곱근 판별 
        long sq = (long)Math.sqrt(n);
      
        if((Math.pow(sq, 2) == n)) {
        	return (long)Math.pow(sq +1 , 2);
        }
        
        return -1;
    }
	
}