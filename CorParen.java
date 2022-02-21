
public class CorParen {
	//¿Ã¹Ù¸¥ °ýÈ£
    boolean solution(String s) {
        boolean answer = true;
        //(()(
        int count = 0;
        char[] str = s.toCharArray();

        for(int i=0;i<str.length;i++) {
        	if(str[i] == '(') {
        		count++;
        	}
        	if(str[i] == ')') {
        		count--;
        	}
        	if(count < 0) {
        		answer = false;
        		break;
        	}
        	if(i >= str.length-1) {
        		if(count != 0) {
        			answer = false;
        		}
        	}
        }
        
        
        return answer;
    }
}
