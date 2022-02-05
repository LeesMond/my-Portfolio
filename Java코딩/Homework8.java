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
		System.out.print("신입사원의 수는 몇명? : ");
		int n = sc.nextInt();
		
		p = new Phone[n];
		for(int i = 0; i<p.length; i++) {
			System.out.print((i+1)+"번째 사원의 이름 입력 :");
			String name = sc.next();
			System.out.print((i+1)+"번째 사원의 번호 입력 :");
			String tel = sc.next();
			System.out.print((i+1)+"번째 사원의 나이 입력 :");
			int age = sc.nextInt();
			
			p[i] = new Phone(name, tel, age);
		}
		System.out.println("모든 사원의 정보를 저장했습니다.");
	}
	
	public void run() {
		read();
		while(true) {
			System.out.print("검색할 사원의 이름 :");
			String name = sc.next();
			
			if(name.equals("exit")) {
				System.out.println("\n 프로그램을 종료합니다...");
				break;
			}
			String tel = tel_Search(name);
			if(tel == null)
				System.out.println(name + "사원은 없습니다");
			else {
				System.out.println(name+" 사원의 전화번호는 "+tel+" 입니다.");
				int age = age_Search(name);
				System.out.println(name+" 사원의 나이는 "+age+" 입니다");
				
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
