
public class MakeBigNumber {
    public String solution(String number, int k) {
        String answer = "";
        
        //index = 0
        //number�� ���� - k ��ŭ �ݺ� ( number - k ��ŭ�� ���̸� Ȯ�� )
        	// index ���� ~ k+i ? ? 
        
        //�ڿ� k���� ���� �����ϰ� ���� �� �߿� ū ���� ã�� -> ū ���� index�� �������� �ݺ�
        
        //4177252841 -> len 10 , for 6 -> �ڿ� 5�ڸ��� Ȯ���ϰ� �տ� �ڸ��� �ݺ�
        // i = 0 , k = 4 , j = 0,  < 4+0 -> 0 1 2 3 4
        // index - ū �� �ε��� ������ �������� �ڿ� �ڸ����� ã�ƾ� ��
        StringBuffer sb = new StringBuffer();
        int index = 0;
        int max = 0;
        for(int i=0;i<number.length()-k;i++) {
        	max = 0;
        	for(int j=index;j<=k+i;j++) {
        		if(max < number.charAt(j)-'0') {
        			max = number.charAt(j)-'0';
        			index = j+1;
        		}
        	}
        	sb.append(max);
        }

        answer = sb.toString();

        return answer;
    }
}
