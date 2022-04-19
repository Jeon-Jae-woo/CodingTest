package IntellijProgrammers;

import java.util.Stack;

public class RemovePairs {

    public static int solution(String s)
    {
        int answer = 0;
        Stack<String> stack = new Stack<String>();

        String first = "";
        String second = "";
        for(int i=0;i<s.length();i++){
            if(stack.isEmpty()){
                stack.push(String.valueOf(s.charAt(i)));
            }else{
                first = stack.peek();
                second = String.valueOf(s.charAt(i));
                if(first.equals(second)){
                    stack.pop();
                }else{
                    stack.push(second);
                }
            }
        }

        if(stack.isEmpty()){
            answer = 1;
        }

        return answer;
    }
    //짝지어 제거하기
    public static void main(String[] args) {
        //같은 알파벳이 붙어있는 경우 제거하고 앞 뒤로 붙임 -> 반복 -> 문자열이 비어있으면 끝 or 마지막이라면 끝
        System.out.println(solution("cdcd"));

    }
}
