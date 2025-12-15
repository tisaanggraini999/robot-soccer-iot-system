float vx, vy, w;

void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');
    sscanf(data.c_str(), "%f,%f,%f", &vx, &vy, &w);

    // Placeholder motor control
    Serial.printf("VX: %.2f VY: %.2f W: %.2f\n", vx, vy, w);
  }
}
