//: exceptions/NeverCaught.java
// Ignoring RuntimeExceptions.
// {ThrowsException}
package exceptions;

public class NeverCaught {
    static void f() {
        throw new RuntimeException("From f()");
    }

    static void g() {
        f();
    }

    public static void main(String[] args) {
        g();
    }
} ///:~
