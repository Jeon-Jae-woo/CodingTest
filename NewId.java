import java.util.ArrayList;

public class NewId {
    public String solution(String new_id) {
        String answer = "";
        
        /*
        1�ܰ� new_id�� ��� �빮�ڸ� �����Ǵ� �ҹ��ڷ� ġȯ�մϴ�.
        2�ܰ� new_id���� ���ĺ� �ҹ���, ����, ����(-), ����(_), ��ħǥ(.)�� ������ ��� ���ڸ� �����մϴ�.
        3�ܰ� new_id���� ��ħǥ(.)�� 2�� �̻� ���ӵ� �κ��� �ϳ��� ��ħǥ(.)�� ġȯ�մϴ�.
        4�ܰ� new_id���� ��ħǥ(.)�� ó���̳� ���� ��ġ�Ѵٸ� �����մϴ�.
        5�ܰ� new_id�� �� ���ڿ��̶��, new_id�� "a"�� �����մϴ�.
        6�ܰ� new_id�� ���̰� 16�� �̻��̸�, new_id�� ù 15���� ���ڸ� ������ ������ ���ڵ��� ��� �����մϴ�.
             ���� ���� �� ��ħǥ(.)�� new_id�� ���� ��ġ�Ѵٸ� ���� ��ġ�� ��ħǥ(.) ���ڸ� �����մϴ�.
        7�ܰ� new_id�� ���̰� 2�� ���϶��, new_id�� ������ ���ڸ� new_id�� ���̰� 3�� �� ������ �ݺ��ؼ� ���� ���Դϴ�.
         */
        
        //step 1
        new_id = new_id.toLowerCase();
        ArrayList<String> sList = new ArrayList<String>();
        char[] tempC = new_id.toCharArray();
        
        //step 2
        for(char c : tempC) {
        	if((c >= '0' && c <= '9') || (c >= 'a' && c <='z')) {
        		sList.add(String.valueOf(c));
        	}else if(c == '-' || c == '_' || c == '.') {
        		sList.add(String.valueOf(c));
        	}
        }
        
        //step 3
        int index = 0;
        while(index < sList.size()) {
        	if(index != sList.size()-1) {
        		if(sList.get(index).equals(".") && sList.get(index+1).equals(".")){
        			sList.remove(index);
        			index=0;
        		}else {
        			index++;
        		}
        	}else {
        		index++;
        	}
        }

        //step 4
        if(sList.size() > 0) {
	        if(sList.get(0).equals(".")) {
	        	sList.remove(0);
	        }
        }
	    if(sList.size() > 0) {
	        if(sList.get(sList.size()-1).equals(".")) {
	        	sList.remove(sList.size()-1);
	        }
	    }
        
        //step 5
        if(sList.size() == 0) {
        	sList.add("a");
        }
        
        //step 6
        answer = String.join("", sList);
        if(answer.length() >= 16) {
        	answer = answer.substring(0,15);
        }
        if(answer.charAt(answer.length()-1) == '.') {
        	answer = answer.substring(0,answer.length()-1);
        }
        
        //step 7
        if(answer.length() <= 2) {
        	while(answer.length() != 3) {
        		answer += answer.substring(answer.length()-1);
        	}
        }
        
        
        return answer;
    }

}
