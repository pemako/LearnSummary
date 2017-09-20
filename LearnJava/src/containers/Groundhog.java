//: containers/Groundhog.java
// Looks plausible, but doesn't work as a HashMap key.
package containers;

public class Groundhog {
    protected int number;

    public Groundhog(int n) {
        number = n;
    }

    public String toString() {
        return "Groundhog #" + number;
    }
} ///:~
