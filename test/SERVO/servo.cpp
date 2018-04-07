#include <iostream>
#include <wiringPi.h>
#include <unistd.h>
using namespace std;

#define PWM_SERVO 	18
#define BUTTON_GPIO	27
#define LEFT		29
#define RIGHT		118
#define CENTER		73
bool sweeping = true;

void buttonPress(void) {
   cout << "Button was pressed -- finishing sweep." << endl;
   sweeping = false;
}

int main() {
   cout << "1" << endl;
   wiringPiSetupGpio();
   cout << "2" << endl;
   pinMode(PWM_SERVO, PWM_OUTPUT);
   cout << "3" << endl;
   pinMode(BUTTON_GPIO, INPUT);
   cout << "4" << endl;
   wiringPiISR(BUTTON_GPIO, INT_EDGE_RISING, &buttonPress);
   cout << "5" << endl;
   pwmSetMode(PWM_MODE_MS);
   pwmSetRange(1000);
   pwmSetClock(384);

   cout << "Sweeping the servo until the button is pressed" << endl;
   while(sweeping) {
      for (int i=LEFT; i<RIGHT; i++) {
         pwmWrite(PWM_SERVO, i);
         usleep(10000);
      }
      for (int i =RIGHT; i<LEFT; i--) {
         pwmWrite(PWM_SERVO, i);
         usleep(10000);
      }
   }
   pwmWrite(PWM_SERVO, CENTER);
   cout << "Program has finished gracefully - servo centered" << endl;
   return 0;
}

