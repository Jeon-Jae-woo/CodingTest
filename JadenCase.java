
public class JadenCase {
    public String solution(String s) {
        StringBuffer sb = new StringBuffer();
        s = s.toLowerCase();
        sb.append(Character.toUpperCase(s.charAt(0)));
        
        for(int i=1;i<s.length();i++) {
        	String temp = String.valueOf(s.charAt(i));
        	if(temp.equals(" ")) {
        		sb.append(" ");
        	}else if(s.charAt(i-1)==' ') {
        		sb.append(temp.toUpperCase());
        	}else {
        		sb.append(temp);
        	}
        }
        
        return sb.toString();
    }
}
