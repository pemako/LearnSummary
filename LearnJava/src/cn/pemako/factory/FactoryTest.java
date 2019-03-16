/**
 * @Time : 23/11/2017 13:19
 * @Email: pemakoa@gmail.com
 */

package cn.pemako.factory;

public class FactoryTest {
    public static void main(String[] args) {
        Factory factory = Factory.getFactory();
        InterfaceTest interObj = factory.getInterface();
        interObj.getName();
    }
}
