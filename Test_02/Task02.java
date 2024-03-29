package Test_02;

public class Task02 {
    public static void main(String[] args) {
        // Используем цикл for, чтобы перебрать числа от 1 до 10
        for (int i = 1; i <= 10; i++) {
            // Проверяем, является ли число четным с помощью оператора %
            if (i % 2 == 0) {
                System.out.println(i);
            }
        }
    }
}
