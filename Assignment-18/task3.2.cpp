#include <iostream>
using namespace std;
int factorial(int n) {
    if (n < 0) {
        cerr << "Error: Factorial is not defined for negative numbers." << endl;
        return -1;
    } else if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Test cases
    cout << "Factorial of 0: " << factorial(0) << endl;
    cout << "Factorial of 5: " << factorial(5) << endl;
    
    return 0;
}
