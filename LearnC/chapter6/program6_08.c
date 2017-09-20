// author <pemakoa@gmail.com>
// Saturday, June 18, 2016 23:02:54 GMT+8

#include <stdio.h>
#include <string.h>

int main(void)
{
	char str1[] = "This string contains the holy grail.";
	char str2[] = "the holy grail";
	char str3[] = "the holy grill";

	if (strstr(str1, str2)) 
		printf("\"%s\" found in \"%s\"\n", str2, str1);
	else
		printf("\"%s\" not found in \"%s\"\n", str2, str1);

	if (strstr(str1, str3))
		printf("\"%s\" found in \"%s\"\n", str3, str1);
	else
		printf("\"%s\" found in \"%s\"\n", str3, str1);

	return 0;
}