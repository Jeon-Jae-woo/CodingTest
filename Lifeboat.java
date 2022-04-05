import java.util.Arrays;

//����Ʈ
public class Lifeboat {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        
        // i -> ��
        // j -> ��
        // people[i] + people[j] > limit --> j-- and count++
        // 						 < limit --> i++, j-- and count++
        // j >= i ---> j==i�� ���� and count++
        int i = 0;
        for(int j=people.length-1;j >= i; j--) {
        	if(people[i]+people[j] > limit) {
        		answer++;
        	}else {
        		i++;
        		answer++;
        	}
        }
        
        return answer;
    }
}
