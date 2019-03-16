/**
 * @Time : 23/11/2017 13:01
 * @Email: pemakoa@gmail.com
 */

package cn.pemako.single;

public class SingRun {
    public static void main(String[] args) {
        Single x = Single.getInstance();
        Single y = Single.getInstance();

        // true 说明两次获得的是同一个对象
        System.out.println(x == y);
    }
}
