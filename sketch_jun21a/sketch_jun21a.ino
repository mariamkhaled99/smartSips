#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <ArduinoOTA.h>

int TDS= 0;
unsigned int tds=0;
#define ONE_WIRE_BUS 2 
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
const uint16_t port = 8585;
const char *host = "192.168.1.11";
WiFiClient client;

void setup()
{
    Serial.begin(115200);
    Serial.println("Connecting...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin("WE_D0FB4F","k8f12274"); // change it to your ussid and password
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    sensors.begin();

    // Set up OTA
    // ArduinoOTA.setHostname("myesp8266"); // Set the hostname
    // ArduinoOTA.setPassword("myota"); // Set the password
    ArduinoOTA.begin();
}

void loop()
{
    ArduinoOTA.handle(); // Handle OTA updates

    if (!client.connect(host, port))
    {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
    sensors.requestTemperatures();
    Serial.println("Connected to server successful!");
    // client.println("Hello From ESP8266");
    
     float temperatureC = sensors.getTempCByIndex(0);
    //  client.print("Temperature: ");
  // client.println(temperatureC);
  // Serial.println("°C");
  // client.print(", TDS: ");
  tds = analogRead(TDS); // read the input pin
 String data = String(tds) + "," + String(temperatureC);
client.println(data);
    // delay(4000);

    while (client.available() > 0)
    {   
        char c = client.read();
        Serial.write(c);
    }

 
    client.stop();
    delay(5000);
}




// #include <ESP8266WiFi.h>
// #include <PubSubClient.h>
// #include <OneWire.h>
// #include <DallasTemperature.h>
// #include <ArduinoOTA.h>

// int TDS = 0;
// unsigned int tds = 0;
// #define ONE_WIRE_BUS 2 
// OneWire oneWire(ONE_WIRE_BUS);
// DallasTemperature sensors(&oneWire);

// const char* ssid = "WE_D0FB4F";
// const char* password = "k8f12274";
// const char* mqtt_server = "localhost";

// WiFiClient espClient;
// PubSubClient client(espClient);

// void setup()
// {
//     Serial.begin(115200);
//     Serial.println("Connecting...\n");
//     WiFi.mode(WIFI_STA);
//     WiFi.begin(ssid, password);
//     while (WiFi.status() != WL_CONNECTED)
//     {
//         delay(500);
//         Serial.print(".");
//     }
//     sensors.begin();

//     // Set up OTA
//     // ArduinoOTA.setHostname("myesp8266"); // Set the hostname
//     // ArduinoOTA.setPassword("myota"); // Set the password
//     ArduinoOTA.begin();

//     client.setServer(mqtt_server, 1883);
// }

// void loop()
// {
//     ArduinoOTA.handle(); // Handle OTA updates

//     if (!client.connected()) {
//         reconnect();
//     }
//     client.loop();

//     sensors.requestTemperatures();
    
//     float temperatureC = sensors.getTempCByIndex(0);
  
//     tds = analogRead(TDS); // read the input pin
//     String data = String(tds) + "," + String(temperatureC);

//     client.publish("your/topic", data.c_str());

//     delay(5000);
// }

// void reconnect() {
//   while (!client.connected()) {
//     Serial.print("Attempting MQTT connection...");
    
//     if (client.connect("ESP8266Client")) {
//       Serial.println("connected");
      
//       client.subscribe("your/subscription/topic");
//     } else {
//       Serial.print("failed, rc=");
//       Serial.print(client.state());
//       Serial.println(" try again in 5 seconds");
      
//       delay(5000);
//     }
//   }
// }