char g;
void setup() {
  // put your setup code here, to run once:
pinMode(2,INPUT);
Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
  int lp= digitalRead(2);
  if(lp==1)
  Serial.println(1);
  if(Serial.available()>0)
  {
    char p= Serial.read();
    Serial.println(2);
  }
}
