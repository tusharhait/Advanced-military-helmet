#include <FreqMeasure.h>


void setup() {
 Serial.begin(9600);
 FreqMeasure.begin();
}

double sum=0;
int count=0;

void loop() {
  if(FreqMeasure.available()){
    sum=sum+FreqMeasure.read();
    count=count+1;
    if(count>30){
      float frequency = FreqMeasure.countToFrequency(sum/count);
      Serial.print(frequency);
      Serial.println(" Hz ");
      Serial.print(frequency/31.36);
      Serial.println("Mph");
      sum=0;
      count=0;
    }
  }
}
