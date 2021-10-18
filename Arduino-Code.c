int incomingByte = 0, Byte=0, red1, green1, blue1, nChar; // for incoming serial data
String stringByte, RGB, rValue, gValue, bValue;

void setup() {
  Serial.begin(500000);
  pinMode(12,OUTPUT);       //R1
  pinMode(14,OUTPUT);       //G1
  pinMode(16,OUTPUT);       //B1
}

void loop() {
  delay(3);
  if (Serial.available() > 0) 
  {
    
    incomingByte = Serial.read();
    
    if(incomingByte!=10){
      Byte=incomingByte-48;
      RGB = RGB + Byte;
      if(Byte==16)
      {
          rValue = RGB.substring(0,3);
          gValue = RGB.substring(3,6);
          bValue = RGB.substring(6,9);
          red1 = rValue.toInt();
          green1 = gValue.toInt();
          blue1 = bValue.toInt();
          analogWrite(12,red1);
          analogWrite(14,green1);
          analogWrite(16,blue1);
          RGB="";
      }
    }
    Serial.println("RGB:" + RGB);
  }

}
