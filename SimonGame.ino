
/*
Simon Game
*/

// defining led pins
#define R 13
#define Y 12
#define B 11
#define G 10

//defining button for each color
#define RB 7
#define YB 6
#define BB 5
#define GB 4

#define WIN 9
#define LOSE 8

//sequence length
#define SQ 5

// setup function
void setup() {
    pinMode(R, OUTPUT);
    pinMode(Y, OUTPUT);
    pinMode(B, OUTPUT);
    pinMode(G, OUTPUT);
    pinMode(WIN, OUTPUT);
    pinMode(LOSE, OUTPUT);
    pinMode(RB, INPUT);
    pinMode(YB, INPUT);
    pinMode(BB, INPUT);
    pinMode(GB, INPUT);
    Serial.begin(9600);

}

int r, y, b, g;

/* declaring an Array with sequence length to store the 
Random evaluated order of LED's */
int lightsArray[SQ];

void blinkALL() {
  for(int i = 10;i<14;i++){
    digitalWrite(i,HIGH);}
  digitalWrite(WIN,HIGH);
  digitalWrite(LOSE,HIGH);
  delay(500);
  for(int i = 10;i<14;i++){
    digitalWrite(i,LOW);}
  digitalWrite(WIN,LOW);
  digitalWrite(LOSE,LOW);
  delay(500);
}
// function that blinks the Win Green light
void winBlink() {
    delay(500);
    digitalWrite(WIN, HIGH);
    delay(500);
    digitalWrite(WIN, LOW);
}

// function that blinks the Lose Red light
void loseBlink() {
    delay(500);
    digitalWrite(LOSE, HIGH);
    delay(500);
    digitalWrite(LOSE, LOW);
}

// function generates 5 random LED's and stores in lightsArray
void randomLights() {
    for (int i = 0; i < SQ; i++) {
        int rand = random(10, 14);
        lightsArray[i] = rand;
    }
}

/* receives input from the user and waits in the while loop
till they hit a bottom */
void inputReceiver() {
    r = 0;
    g = 0;
    y = 0;
    b = 0;
    while (r == 0 && y == 0 && 
           b == 0 && g == 0) {
        Serial.print(" ");
        r = digitalRead(RB);
        y = digitalRead(YB);
        b = digitalRead(BB);
        g = digitalRead(GB);
    }
}

// main loop function
void loop() {
    blinkALL();
  	blinkALL();
    // declaring lost as 0 (meaning false)
    int lost = 0;

    // generating random lights
    randomLights();

    // prints the order in the console just to check
    for (int x = 0; x < SQ; x++) {
        Serial.print(lightsArray[x]);
        Serial.print(" ");
    }

    // loops from 1 to the number of sequence and has a 1sec delay after each loop
    for (int i = 1; i <= SQ; i++) {
        delay(1000);
        Serial.print("\n");

        // blinks LEDs according to the Array order 
        for (int k = 0; k < i; k++) {
            digitalWrite(lightsArray[k], HIGH);
            delay(500);
            digitalWrite(lightsArray[k], LOW);
            delay(500);
        }

        // receives input from the user
        for (int k = 0; k < i; k++) {

            // printing variables just to confirm in the monitor
            Serial.print("k: ");
            Serial.println(k);
            Serial.print("lightsArray: ");
            Serial.println(lightsArray[k]);
            r = 0;
            g = 0;
            y = 0;
            b = 0;
            Serial.print("BEFORE: ");
            Serial.print(r);
            Serial.print(y);
            Serial.print(b);
            Serial.print(g);
            Serial.println();
            Serial.println("Receiving INPUT");
            delay(100);

            // receives input from the user k times in loop
            inputReceiver();
            Serial.print("AFTER: ");
            Serial.print(r);
            Serial.print(y);
            Serial.print(b);
            Serial.print(g);
            Serial.println();


            // checks whether the user's input is in the order of the array
            if (lightsArray[k] == R && r == 1) {
              digitalWrite(R,HIGH);
              delay(500);
              digitalWrite(R,LOW);
                continue;
            } else if (lightsArray[k] == Y && y == 1) {
              digitalWrite(Y,HIGH);
              delay(500);
              digitalWrite(Y,LOW);
                continue;
            } else if (lightsArray[k] == B && b == 1) {
              digitalWrite(B,HIGH);
              delay(500);
              digitalWrite(B,LOW);
                continue;
            } else if (lightsArray[k] == G && g == 1) {
              digitalWrite(G,HIGH);
              delay(500);
              digitalWrite(G,LOW);
                continue;
            } else {
			  if (r == 1) {
             digitalWrite(R,HIGH);
              delay(500);
              digitalWrite(R,LOW);
            
            } else if (y == 1) {
              digitalWrite(Y,HIGH);
              delay(500);
              digitalWrite(Y,LOW);
                
            } else if (b == 1) {
              digitalWrite(B,HIGH);
              delay(500);
              digitalWrite(B,LOW);
                
            } else if (g == 1) {
              	digitalWrite(G,HIGH);
              	delay(500);
              	digitalWrite(G,LOW);
              }
                // prints a message when they lose and blinks the red light
                Serial.println("YOU LOST");
                loseBlink();

                // lost becomes 1 (True) and breaks the first loop
                lost++;
                break;
            
            }
            if (lost == 1) {
                break;
            } else {
                continue;
            }
            r = 0;
            g = 0;
            y = 0;
            b = 0;

        }
        if (lost == 1) {
            break;
        }

        // if the user reaches the end the winning light will blink 
        if (i == SQ) {
            winBlink();
        }
    }

    // after 2 seconds the game resets 
    delay(2000);

    Serial.println("GAME RESETS");

}
