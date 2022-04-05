import java.util.HashMap;

public class PhoneNumberList {
	//��ȭ��ȣ ���
    public boolean solution(String[] phone_book) {
        boolean answer = true;

        // hashMap �ȿ� ��� ����  put  
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        
        for(int i=0;i<phone_book.length;i++) {
        	hm.put(phone_book[i], 0);
        }
        
        //���ڿ��� �߶� �� (�տ������� ����������) 
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
