package intellijBaekjoon;

import java.util.Scanner;

//실패
//백트래킹 --> 추후 DFS 적용하여 수정계획
public class B15649 {
    //N과 M(1)
    public static void main(String[] args) {
        //1~N까지 중복없이 M개 구하기
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        String numbers;
        for(int i=1;i<=n;i++){
            numbers = String.valueOf(i); // 초기화
            for(int j=1;j<=m;j++){
                for(int z=1;z<=n;z++){
                    if(!numbers.contains(String.valueOf(z))){
                        System.out.print(i+" "+z);
                        numbers +=z;
                    }
                }
                System.out.println();
            }
        }

    }
}
//숫자를 출력하는데 --> 문자열에 숫자 추가 and 해당 문자열에 숫자가 존재하지 않는 경우에만 추가?
//for -> m 만큼 반복 --> 가로 횟수
// for ( n 까지 ) --> m번째 자리에 들어갈 숫자를 찾는 작업