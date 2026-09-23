int pir = 2;
int led = 8;
int buzzer = 9;

int previousMotion = LOW;

void setup()
{
  pinMode(pir, INPUT);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);

  // Give PIR time to stabilize
  delay(30000);
}

void loop()
{
  int motion = digitalRead(pir);

  // Send only when PIR state changes
  if (motion != previousMotion)
  {
    if (motion == HIGH)
    {
      Serial.println("MOTION");
    }
    else
    {
      Serial.println("NO_MOTION");
    }

    previousMotion = motion;
  }

  // Receive command from Python
  if (Serial.available() > 0)
  {
    char command = Serial.read();

    if (command == '1')
    {
      digitalWrite(led, HIGH);
      digitalWrite(buzzer, HIGH);
    }
    else if (command == '0')
    {
      digitalWrite(led, LOW);
      digitalWrite(buzzer, LOW);
    }
  }

  delay(1000);
}