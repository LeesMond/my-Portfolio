import java.util.Scanner;

public class Homework1 {

	public static void main(String[] args) {
		String kor[] = {"�л�", " ���", "�ڹ�", "�ູ��", "�̷�"};
		String eng[] = {"student", "love", "java", "happy", "future"};
		
		Scanner s = new Scanner(System.in);
		String w;
		
		while(true) {
			System.out.print("���� �ܾ �Է��ϼ��� : ");
			w = s.next();
			
			if(w.equals("exit")) {
				System.out.println("�����մϴ�...");
				break;
			}
			int i;
			for(i=0; i<eng.length; i++) {
				if(eng[i].equals(w)) {
					System.out.println(kor[i]);
					break;
				}
			}
			if(i == eng.length) {
				System.out.println("�׷� ���ܾ �����ϴ�.");
			}
		}

	}

}
