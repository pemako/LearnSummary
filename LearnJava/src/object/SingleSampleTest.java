/**
 * @Time : 05/09/2017 01:09
 * @Email: pemakoa@gmail.com
 */

package object;

import org.testng.annotations.Test;

public class SingleSampleTest {

    @Test
    public static  void TestSingle() {
        SingleSample in = SingleSample.getInstance();
        SingleSample in2 = SingleSample.getInstance();
        System.out.println(in == in2);
    }
}
