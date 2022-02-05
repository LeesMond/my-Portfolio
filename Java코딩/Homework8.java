import java.util.Scanner;

class Phone{
	private String name;
	private String tel;
	private int age;
	
	public Phone(String name, String tel, int age) {
		this.name = name;
		this.tel = tel;
		this.age = age;
	}
	
	public String getName() {return this.name;}
	public String getTel() {return this.tel;}
	public int getAge() {return this.age;}
	
}	

public class Homework8 {
	private Scanner sc;
	private Phone[] p;

	public Homework8() {
		sc = new Scanner(System.in);
	}
	private void read() {
		System.out.print("���Ի���� ���� ���? : ");
		int n = sc.nextInt();
		
		p = new Phone[n];
		for(int i = 0; i<p.length; i++) {
			System.out.print((i+1)+"��° ����� �̸� �Է� :");
			String name = sc.next();
			System.out.print((i+1)+"��° ����� ��ȣ �Է� :");
			String tel = sc.next();
			System.out.print((i+1)+"��° ����� ���� �Է� :");
			int age = sc.nextInt();
			
			p[i] = new Phone(name, tel, age);
		}
		System.out.println("��� ����� ������ �����߽��ϴ�.");
	}
	
	public void run() {
		read();
		while(true) {
			System.out.print("�˻��� ����� �̸� :");
			String name = sc.next();
			
			if(name.equals("exit")) {
				System.out.println("\n ���α׷��� �����մϴ�...");
				break;
			}
			String tel = tel_Search(name);
			if(tel == null)
				System.out.println(name + "����� �����ϴ�");
			else {
				System.out.println(name+" ����� ��ȭ��ȣ�� "+tel+" �Դϴ�.");
				int age = age_Search(name);
				System.out.println(name+" ����� ���̴� "+age+" �Դϴ�");
				
			}
		}
	}
	private String tel_Search(String name) {
		for(int i = 0; i<p.length;i++) {
			if(p[i].getName().equals(name))
				return p[i].getTel();
		}
		return null;
	}
	private int age_Search(String name) {
		for(int i = 0; i<p.length; i++) {
			if(p[i].getName().equals(name))
				return p[i].getAge();
		}
		return 0;
	}
	public static void main(String[] args) {
		new Homework8().run();

	}

}
