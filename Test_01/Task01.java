package Test;
import java.util.Scanner;

public class Task01 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Запрос ввода от пользователя
        System.out.println("Введите количество секунд: ");
        int seconds = scanner.nextInt();

        // Форматирование секунд
        String formattedSeconds = formatSeconds(seconds);

        // Вывод отформатированных секунд
        System.out.println(formattedSeconds);
    }

    public static String formatSeconds(int seconds) {
        int days = seconds / 86400;
        seconds %= 86400;
        int hours = seconds / 3600;
        seconds %= 3600;
        int minutes = seconds / 60;
        seconds %= 60;

        return days + " days " + hours + " hours " + minutes + " minutes " + seconds + " seconds";
    }
}