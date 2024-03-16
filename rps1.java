import java.util.Scanner;
import java.util.Random;
public class rps1{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        Random random = new Random();
        System.out.println("Wanna play Rock, Paper and Scissors?\n Choose one\n 1. Play \n 2. Nah, I will pass.");
        int start = input.nextInt();
        if (start == 1){
            int win = 0;
            int lose = 0;
            int draw = 0;
            System.out.println("We gonna play five time. Whoever wins the most is winner.");
            for (int i = 0; i < 5; i++){
                System.out.println(" 1. Rock \n 2. Paper \n 3. Scissors ");
                int u_choice = input.nextInt();
                int c_choice = random.nextInt(2)+1;
                if ( u_choice == c_choice){
                    System.out.println("It's a draw");
                    draw++;
                }
                else if(u_choice == 1 && c_choice == 2 || u_choice == 2 && c_choice == 3 || u_choice == 3 && c_choice == 1){
                    System.out.println("You lost this round");
                    lose++;
                }
                else{
                    System.out.println("You won this round");
                    win ++;
                }
                 
            }
            System.out.println("Win = "+win+ "     Lose = "+lose+"      Draw = "+draw);
            if ( win > lose){
                System.out.println("You won the game");
            }
            else{
                System.out.println("Sorry, but you lost the game. Better luck next time");
            }
        }
        else{
            System.out.print("Come back whenever you're in mood to play");
        }

        input.close();
    }
}