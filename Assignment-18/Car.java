public class Car {
    // Attributes
    private String brand;
    private String model;
    private int year;
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }
    
    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("Brand: " + this.brand);
        System.out.println("Model: " + this.model);
        System.out.println("Year: " + this.year);
    }
    
    public static void main(String[] args) {
        // Create an object and call the method
        Car car = new Car("Toyota", "Corolla", 2020);
        car.displayDetails();
    }
}
