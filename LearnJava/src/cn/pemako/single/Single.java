/**
 * @Time : 23/11/2017 11:40
 * @Email: pemakoa@gmail.com
 */

/**
 * 单例模式（Singleton）
 * 保证在 Java 应用程序中，一个类 Class 只有一个示例存在
 * 单例模式要求保证唯一，可以通过静态变量保证单例模式的唯一性
 *
 * 单例模式有两种形式，第一种形式如下
 */
package cn.pemako.single;

public class Single {
    /**
     * 注意这是 private 私有的构造方法，只供内部调用，外部不能通过 new 的方式来
     * 生成该类的实例
     */
    private Single(){}

    /**
     * 在自己内部定义自己的一个实例，定义静态实例，保证其唯一性
     */
    private static Single instance = new Single();

    /**
     * 提供外部访问本 class 的静态方法，
     */
    public static Single getInstance() {
        return instance;
    }
}
