/**
 * @Time : 23/11/2017 13:02
 * @Email: pemakoa@gmail.com
 */

package cn.pemako.single;

public class Single2 {
    // 先声明该类静态对象
    private static Single2 instance = null;

    // 创建一个静态访问器，获得该类实例，加上同步机制，放置两个线程同时进行对象的创建
    public static synchronized Single2 getInstance(){
        if (instance == null) {
            return new Single2();
        }
        return instance;
    }
}
