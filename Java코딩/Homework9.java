import java.util.Scanner;

class Player{
	private String name;
	private Scanner sc = new Scanner (System.in);
	public Player(String name) {
		this.name = name;
	}
	public String getName() {
		return name;
	}
	public int turn() {
		System.out.print(name + "1. ����, 2. ����, 3.�� �Է� >>");
		return sc.nextInt();
	}
}

class Com extends Player{
	public Com(String name) {
		super(name);
	}
	public int turn() {
		return (int)(Math.random()*3+1);
	}
}
public class Homework9 {
	private final String s[] = {"����", "����", "��"};
	
	private Player ps[] = new Player[2];
	public Homework9() {
		ps[0] = new Player("�̼���");
		ps[1] = new Com("��ǻ��");
	}
	
	public void run() {
		int user;
		int computer;
		int win = 0, draw = 0, lose = 0, tot = 0;
		while(true) {
			user = ps[0].turn();
			if(user == 4)
				break;
			computer = ps[1].turn();
			if(user < 1 || user > 4)
				System.out.println("�߸� �Է��ϼ̽��ϴ�.");
			else {
				System.out.print(ps[0].getName()+"("+s[user-1]+") vs ");
				System.out.print(ps[1].getName()+"("+s[computer-1]+")");
				
				if((user == 1 && computer ==3)||(user ==2 && computer == 1)||(user == 3 && computer ==2)) {
					System.out.println(ps[0].getName()+"�¸�");
					win++;
					tot++;
				}
				else if(user == computer) {
					System.out.println("���º�");
					draw++;
					tot++;
				}
				else {
					System.out.print(ps[1].getName()+"�¸�");
					lose++;
					tot++;
				}
			}
			System.out.println(tot + "�� " + win + "�� " + draw + "�� " + lose + "��\n");
		}
	}
	public static void main(String[] args) {
		Homework9 rg = new Homework9();
		rg.run();

	}

}
