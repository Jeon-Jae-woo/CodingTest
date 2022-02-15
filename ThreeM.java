
public class ThreeM {
	
    public int solution(int n) {
        StringBuffer sb = new StringBuffer();
        
        while(n > 0) {
        	sb.append(n%3);
        	n /=3;
        }
        
        return Integer.parseInt(sb.toString(), 3);
    }
}

