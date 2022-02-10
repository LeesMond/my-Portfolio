import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Finaltest extends JFrame{
	ImageIcon [] img = {new ImageIcon("1.png"), new ImageIcon("2.png"), new ImageIcon("3.png"),
			 new ImageIcon("4.png"), new ImageIcon("5.png")};
	
	JLabel imageLabel;
	JButton left;
	JButton right;
	int in;
	
	public Finaltest() {
		setTitle("이미지 뷰어 프로그램 21741024 이종무");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();	
		
		in = 0;
		
		MenuPanel menuPanel = new MenuPanel();
		Photo photo = new Photo();
		
		c.add(menuPanel, BorderLayout.SOUTH);
		c.add(photo, BorderLayout.CENTER);
		
		setSize(400,500);
		setVisible(true);
	}
	
	class MenuPanel extends Panel{
		MenuPanel(){
			setBackground(Color.LIGHT_GRAY);
			left = new JButton(new ImageIcon("l.png"));
			right = new JButton(new ImageIcon("r.png"));
			left.addActionListener(new lmgL());
			right.addActionListener(new lmgL());
			add(left);
			add(right);
		}
	}
	
	class Photo extends Panel{
		Photo(){
			imageLabel = new JLabel();
			imageLabel.setIcon(img[in]);
			add(imageLabel);
		}
	}
	
	
	class lmgL implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			if(e.getSource().equals(left))
				indexReturn(-1);
			else
				indexReturn(1);
			imageLabel.setIcon(img[in]);
		}
	}
	
	public void indexReturn(int d) {
		if(d == 1)
			if(in < 4)
				in++;
			else
				in = 0;
			else if(d == -1)
				if(in > 0)
						in--;
			else
				in = 4;
	}
	
	public static void main(String[] args) {
		new Finaltest();

	}

}
