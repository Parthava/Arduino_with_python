const int LED=9;
char data;

void setup()
{
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available()>0)
  {
    data=Serial.read();
    Serial.println(data);
  }
  if(data=='1')
  {
    digitalWrite(LED,HIGH);
  }
  else if(data=='0')
  {
    digitalWrite(LED,LOW);
  }
}
