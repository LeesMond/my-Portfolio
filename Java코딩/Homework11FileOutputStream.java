import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class Homework11FileOutputStream {

	public static void main(String[] args) {
		byte b[];
		b = new byte[6];
		Scanner x = new Scanner(System.in);
		System.out.print("���� 6���� �Է����ּ��� : ");
		for(int i = 0; i<b.length; i++) {
			b[i] = x.nextByte();
		}
		for(int i = 0; i<b.length; i++) {
			System.out.print(b[i]+" ");
		}
		try {
			FileOutputStream fout = new FileOutputStream("c:\\Temp\\test.out");
			for(int i = 0; i<b.length; i++)
				fout.write(b[i]);
			fout.close();
		}catch(IOException e) {}
		System.out.println("c\\Temp �� test.out.�� �����Ͽ����ϴ�.");
	}

}
