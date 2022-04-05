import java.util.HashMap;

public class PhoneNumberList {
	//전화번호 목록
    public boolean solution(String[] phone_book) {
        boolean answer = true;

        // hashMap 안에 모든 원소  put  
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        
        for(int i=0;i<phone_book.length;i++) {
        	hm.put(phone_book[i], 0);
        }
        
        //문자열을 잘라서 비교 (앞에서부터 마지막까지) 
        for(int i=0;i<phone_book.length;i++) {
        	for(int j=0;j<phone_book[i].length();j++) {
        		if(hm.containsKey(phone_book[i].substring(0,j))) {
        			answer = false;
        			break;
        		}
        	}
        }
        
        return answer;
        
    }
}
