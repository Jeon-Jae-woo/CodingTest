package IntellijProgrammers;

import java.util.Arrays;
import java.util.Comparator;

public class LargestNumber {
    //가장 큰 수
    public static String solution(int[] numbers) {
        //정렬
        String answer = "";

        //compare 문자 정렬 사용
        String[] strList = new String[numbers.length];
        for(int i=0;i<numbers.length;i++){
            strList[i] = String.valueOf(numbers[i]);
        }

        Arrays.sort(strList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2+o1).compareTo(o1+o2);
            }
        });

        //0인 경우
        if(strList[0].equals("0")){
            answer = "0";
        }else{
            for(String str : strList){
                answer += str;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] numbers = {3, 30, 34, 5, 9};
        System.out.println(solution(numbers));
    }

}
