// author <pemakoa@gmail.com>
// Wednesday, June 15, 2016 23:03:07 GMT+8

// 定义一个数组 data 它包含100个 double 类型的元素。编写一个循环
// 将一下的数值序列存储到数组的对应元素中：
// 1/(2*3*4) 1/(4*5*6) .... up 1/(200*201*202)
// 编写另一个循环，计算
//  data[0] - data[1] + data[2] - data[3] + ... -data[99]
//  将这个结果乘以 4.0 加上3.0 输出最后的结果

#include <stdio.h>

int main(void)
{
	double data[100];
	double sum = 0.0;
	double sign = 1.0;

	int j = 0;
	for (int i = 0; i < 100; i++) {
		j = 2 * (i + 1);
		data[i] = 1.0 / (j * (j +1) * (j + 2));
		sum += sign*data[i];
		sign = -sign;
	}

	printf("The result is %.4f\n", 4.0*sum + 3.0);
	return 0;
}