/**
 * @Time : 05/09/2017 01:08
 * @Email: pemakoa@gmail.com
 */

package object;

public class SingleSample {

    private static SingleSample instance = new SingleSample();

    public static SingleSample getInstance() {
        return instance;
    }
}
