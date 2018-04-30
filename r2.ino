char g;
void setup() {
  // put your setup code here, to run once:
pinMode(2,INPUT);
Serial.begin(9600);
}
void loop() {
  // put your main code here, to run repeatedly:
   g=digitalRead(2);
   if(g==1)
   Serial.println(2);
}
