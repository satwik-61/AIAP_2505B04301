public class Task21 {
    
    /**
     * Checks if a number is positive, negative, or zero.
     * @param num the number to check
     */
    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is a positive number.");
        } else if (num < 0) {
            System.out.println(num + " is a negative number.");
        } else {
            System.out.println(num + " is zero.");
        }
    }
    
    public static void main(String[] args) {
        checkNumber(5);
        checkNumber(-3);
        checkNumber(0);
    }
}
