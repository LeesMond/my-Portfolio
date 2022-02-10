import java.util.Scanner;

public class Homework {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int A[];
		A = new int[10];
		System.out.println("정수 10개 입력");
		for(int i=0; i<A.length;i++) {
			A[i] = s.nextInt();
			if(A[i]%3==0) {
				System.out.print(A[i]+" ");
			}
		}

	}

}
