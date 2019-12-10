//============================智宇科技===========================
//  智能小车前后左右综合实验
//===============================================================
//#include <Servo.h> 
int Left_motor=8;     //左电机(IN3) 输出0  前进   输出1 后退
int Left_motor_pwm=9;     //左电机PWM调速

int Right_motor_pwm=10;    // 右电机PWM调速
int Right_motor=11;    // 右电机后退(IN1)  输出0  前进   输出1 后退
int x=0;

void setup()
{
  //初始化电机驱动IO为输出方式
    Serial.begin(9600);

  pinMode(Left_motor,OUTPUT); // PIN 8 8脚无PWM功能
  pinMode(Left_motor_pwm,OUTPUT); // PIN 9 (PWM)
  pinMode(Right_motor_pwm,OUTPUT);// PIN 10 (PWM) 
  pinMode(Right_motor,OUTPUT);// PIN 11 (PWM)
}
void back(int time)     // 前进
{
  digitalWrite(Right_motor,LOW);  // 右电机前进
  digitalWrite(Right_motor_pwm,HIGH);  // 右电机前进     
  analogWrite(Right_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  
  
  digitalWrite(Left_motor,LOW);  // 左电机前进
  digitalWrite(Left_motor_pwm,HIGH);  //左电机PWM     
  analogWrite(Left_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);   //执行时间，可以调整  
}

void brake(int time)         //刹车，停车
{
  
  digitalWrite(Right_motor_pwm,LOW);  // 右电机PWM 调速输出0      
  analogWrite(Right_motor_pwm,0);//PWM比例0~255调速，左右轮差异略增减

  digitalWrite(Left_motor_pwm,LOW);  //左电机PWM 调速输出0          
  analogWrite(Left_motor_pwm,0);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);//执行时间，可以调整  
}

void left(int time)         //左转(左轮不动，右轮前进)
{
  digitalWrite(Right_motor,LOW);  // 右电机前进
  digitalWrite(Right_motor_pwm,HIGH);  // 右电机前进     
  analogWrite(Right_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  
  
  digitalWrite(Left_motor,LOW);  // 左电机前进
  digitalWrite(Left_motor_pwm,LOW);  //左电机PWM     
  analogWrite(Left_motor_pwm,0);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);	//执行时间，可以调整  
}

void spin_left(int time)         //左转(左轮后退，右轮前进)
{
  digitalWrite(Right_motor,LOW);  // 右电机前进
  digitalWrite(Right_motor_pwm,HIGH);  // 右电机前进     
  analogWrite(Right_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  
  digitalWrite(Left_motor,HIGH);  // 左电机后退
  digitalWrite(Left_motor_pwm,HIGH);  //左电机PWM     
  analogWrite(Left_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);	//执行时间，可以调整  
}

void right(int time)        //右转(右轮不动，左轮前进)
{
   digitalWrite(Right_motor,LOW);  // 右电机不转
  digitalWrite(Right_motor_pwm,LOW);  // 右电机PWM输出0     
  analogWrite(Right_motor_pwm,0);//PWM比例0~255调速，左右轮差异略增减
  
  
  digitalWrite(Left_motor,LOW);  // 左电机前进
  digitalWrite(Left_motor_pwm,HIGH);  //左电机PWM     
  analogWrite(Left_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);	//执行时间，可以调整  
}

void spin_right(int time)        //右转(右轮后退，左轮前进)
{
  digitalWrite(Right_motor,HIGH);  // 右电机后退
  digitalWrite(Right_motor_pwm,HIGH);  // 右电机PWM输出1     
  analogWrite(Right_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  
  
  digitalWrite(Left_motor,LOW);  // 左电机前进
  digitalWrite(Left_motor_pwm,HIGH);  //左电机PWM     
  analogWrite(Left_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);	//执行时间，可以调整    
}

void run(int time)          //后退
{
  digitalWrite(Right_motor,HIGH);  // 右电机后退
  digitalWrite(Right_motor_pwm,HIGH);  // 右电机前进     
  analogWrite(Right_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  
  
  digitalWrite(Left_motor,HIGH);  // 左电机后退
  digitalWrite(Left_motor_pwm,HIGH);  //左电机PWM     
  analogWrite(Left_motor_pwm,150);//PWM比例0~255调速，左右轮差异略增减
  delay(time * 100);   //执行时间，可以调整    
}

// the loop routine runs over and over again forever:
void loop(){

  if (Serial.available() > 1){
  x = Serial.read();
  Serial.println(x, DEC);
  //delay(1);
  brake(1);
    if (x == 49){
      Serial.println("Virar direita");
      right(0.1);
      delay(100);
      brake(0.1);
    } else if (x == 50){
      Serial.println("Virar esquerda");
      left(0.1);
      delay(100);
      brake(0.1);
    } else if (x == 51){
      Serial.println("Seguir em frente");
      run(0.1);
      delay(100);
      brake(0.1);
    } else if (x == 52){
      Serial.println("Ir para tras");
      back(0.1);
      delay(100);
      brake(0.1);
    } else {
      brake(0.1);
    }

}}
