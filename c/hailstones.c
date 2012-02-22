#include <stdio.h>

void hailstone(int n)
{
	printf("%i\n", n);
	if (n == 1)
	{
		return;
	}
	if (n % 2 ==0)
	{
		hailstone(n / 2);
	}
	else
	{
		hailstone(3*n + 1);
	}
}

int main(int argc, char ** argv)
{
	if (argc < 2)
	{
		printf("Usage:\n");
		printf("hailstone x\n");
		printf("\nPrint the hailstone sequence for x\n");
		return 0;
	}
	int start = atoi(argv[1]);
	hailstone(start);
	return 0;
}
