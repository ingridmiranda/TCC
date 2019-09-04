int x = 0;
int led1 = 13;
int led2 = 12;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop(){

  if (Serial.available() > 1){
  x = Serial.read();
  Serial.println(x, DEC);
  delay(1);
    if (x == 50){
      Serial.println("Virar direita");
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      delay(100);
      digitalWrite(led1, LOW);
    } else if (x == 49){
      Serial.println("Virar esquerda");
      digitalWrite(led2, HIGH);
      digitalWrite(led1, LOW);
      delay(100);
      digitalWrite(led1, LOW);
    }

}}
