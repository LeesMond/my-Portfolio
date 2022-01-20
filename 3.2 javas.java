import java.util.Scanner;

class Rect{
    private int width, height;
    public Rect(int width, int height){
        this.width = width;
        this.height = height;
    }
    public int getArea(){
        return width*height;
    }
}

public class RectArray{
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        Rect[] arr = new Rect[4];
        int a = 0;

        for(int i = 0; i < 4; i++){
            System.out.print(i + 1 + " 너비와 높이 >>");
            arr[i] = new Rect(num.nextInt(), num.nextInt());
            a += arr[i].getArea();
        }
        System.out.println("저장 하였습니다...");
        System.out.println("사각형의 전체 합은 : " + a);
    }
}