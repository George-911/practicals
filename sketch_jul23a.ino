// Diode Signal Detector using ESP32
const int signalPin = 25;  // GPIO pin connected after the diode

void setup() {
  Serial.begin(115200);          // Start serial communication
  pinMode(signalPin, INPUT);     // Configure the signal pin as input
}

void loop() {
  int signalState = digitalRead(signalPin);  // Read the signal state

  if (signalState == HIGH) {
    Serial.println("High voltage detected!");
  } else {
    Serial.println("No high voltage detected (safe).");
  }

  delay(500);  // Wait for half a second before next read
}

