import java.util.Scanner;

public class Homework7 {
	String title, author, money;
	
	public Homework7() {
		this("","","");
		System.out.println("å�̸��� ���ڸ� �Է� ���� ��� ����");
	}
	
	public Homework7 (String title, String author, String money) {
		this.title = title;
		this.author = author;
		this.money = money;
	}
	
	public static void main(String[] args) {
		Homework7 Homework7[] = new Homework7[2];
		Homework7 b = new Homework7();
		
		Scanner sc = new Scanner(System.in);
		
		for(int i = 0; i<Homework7.length; i++) {
			System.out.print((i+1)+"��° å ����>> ");
			String title = sc.nextLine();
			
			System.out.print((i+1)+"��° å ����>> ");
			String author = sc.nextLine();
			
			System.out.print((i+1)+"��° å ����>> ");
			String money = sc.nextLine();
			
			Homework7[i] = new Homework7(title, author, money);
		}
		
		for(int i = 0; i < Homework7.length; i++) {
			System.out.println("<"+Homework7[i].title+", "+Homework7[i].author+", "+Homework7[i].money+">");
		}
		sc.close();
	}

}
