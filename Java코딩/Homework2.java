import java.util.Scanner;

public class Homework2 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str[] = {"����", "����", "��"};
		
		System.out.println("��ǻ�Ϳ� ���������� ������ �մϴ�");
		
		while(true) {
			System.out.println("���� ���� ��! >>");
			String what = s.next();
			
			int n = (int)(Math.random()*3);
			
			if(what.equals("�׸�"))
				break;
			
			if(str[n].equals("����")) {
				if(what.equals("����"))
					System.out.println("����� : " + what + ", ��ǻ�� : ���� = �����ϴ�.");
				else if(what.equals("����"))
					System.out.println("����� : " + what + ", ��ǻ�� : ���� = �̰���ϴ�.");
				else if(what.equals("��"))
					System.out.println("����� : " + what + ", ��ǻ�� : ���� = �����ϴ�.");
			}
			if(str[n].equals("����")) {
				if(what.equals("����"))
					System.out.println("����� : " + what + ", ��ǻ�� : ���� = �����ϴ�.");
				else if(what.equals("����"))
					System.out.println("����� : " + what + ", ��ǻ�� : ���� = �����ϴ�.");
				else if(what.equals("��"))
					System.out.println("����� : " + what + ", ��ǻ�� : ���� = �̰���ϴ�.");
			}
			if(str[n].equals("��")) {
				if(what.equals("����"))
					System.out.println("����� : " + what + ", ��ǻ�� : �� = �̰���ϴ�.");
				else if(what.equals("����"))
					System.out.println("����� : " + what + ", ��ǻ�� : �� = �����ϴ�.");
				else if(what.equals("��"))
					System.out.println("����� : " + what + ", ��ǻ�� : �� = �����ϴ�.");
			}
		}
		System.out.println("������ �����մϴ�...");
		s.close();
	}

}
