#include <signal.h>
#include <stdlib.h>
#include <wiringPi.h>
#include "../motor.h"

void handler(int signum)
{
	motor_stop();
	delay(100);
	exit(1);
}


int main()
{
	signal(SIGINT, handler);
	pwm_initialize();
	motor_forward(60);
	delay(5000);
	motor_right(50);
	delay(5000);
	motor_left(50);
	delay(5000);
	motor_back(50);
	delay(5000);
	motor_stop();
	delay(100);
}
