import java.util.Scanner;

class Rect{
	private int width, height;
	public Rect(int width, int height) {
		this.width = width;
		this.height = height;
	}
	public int getArea() {
		return width * height;
	}
}


public class Homework3 {

	public static void main(String[] args) {
		Scanner num = new Scanner(System.in);
		Rect[] arr = new Rect[4];
		int a = 0;
		
		for(int i = 0; i<4; i++) {
			System.out.print(i+1+"�ʺ�� ���� >>");
			arr[i] = new Rect(num.nextInt(), num.nextInt());
			a += arr[i].getArea();
		}
		System.out.println("����Ǿ����ϴ�.");
		System.out.println("�簢���� ��ü ���� : "+a);

	}

}
