/**
 * @Time : 23/11/2017 13:09
 * @Email: pemakoa@gmail.com
 */

// 工厂类，生产接口对象

package cn.pemako.factory;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Factory {
    // 创建私有的静态的 Properties 对象
    private static Properties prop=new Properties();



    // 单例测试，保证该类只有一个 Factory 对象
    private static Factory factory = new Factory();
    static { // 静态代码块，在创建这个类的示例之前执行，且只执行一次，用来加载配置文件
        try {
            InputStream ips = Factory.class.getClassLoader().getResourceAsStream("/Users/lena/Desktop/LearnSummary/LearnJava/src/cn/pemako/factory/file.properties");
            prop.load(ips);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private Factory(){}
    public static Factory getFactory(){
        return factory;
    }

    public InterfaceTest getInterface() {
        InterfaceTest interfaceTest = null;
        try {
            // 根据健，获取值，
            String classInfo = prop.getProperty("test");
            // 利用反射，生成 Class 对象
            Class<?> c = Class.forName(classInfo);
            // 获得 Class 对象的实例
            Object obj = c.newInstance();
            // 将 Object 对象强制转为接口对象
            interfaceTest = (InterfaceTest)obj;
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        }
        return interfaceTest;
    }
}
