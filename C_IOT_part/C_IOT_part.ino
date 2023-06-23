
#include <OneWire.h>
#include <DallasTemperature.h>





int TDS= 0;
unsigned int tds=0;
#define ONE_WIRE_BUS 2 
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);


void setup(void) {
  // initialize the Serial Monitor at a baud rate of 9600.
  Serial.begin(9600);
  sensors.begin();
 
}

void loop(void) {
 
  sensors.requestTemperatures();
  
  float temperatureC = sensors.getTempCByIndex(0);
  Serial.print("Temperature: ");
  Serial.print(temperatureC);
  // Serial.println("°C");
  Serial.print(", TDS: ");
  tds = analogRead(TDS); // read the input pin
  Serial.println( tds);
  

  delay(1000);
}