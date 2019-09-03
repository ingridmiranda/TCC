int x = 0;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop(){
  if (Serial.available() > 1){
  x = Serial.read();
  Serial.println(x, DEC);
  delay(1);
    if (x == 50){
      Serial.println("Virar direita");
    } else if (x == 49){
      Serial.println("Virar esquerda");
    } 


}}
