/**
 * Gathering and Graphing Data Using the TSL1402R
 *
 * VERSION D
 *
 * Scott Prahl
 * November 2013
 */

import processing.serial.*;
Serial port;
PFont f;
int xSize = 800;
int ySize = 600;
int fontsize = 24;
int[] data;
int[] bdata;
color OIT_BLUE = color(0, 55, 103);
color OIT_YELLOW = color(255, 210, 79);

void setup() {
    size(int(xSize+10*fontsize), int(ySize+8*fontsize));

    // Create the font
    println(PFont.list());
    f = createFont("FranklinGothic-Medium", fontsize);
    textFont(f);

    data = new int[256];
    bdata = new int[512];
    for (int i=0; i<256; i++)
        data[i] = int(512 + 256 * sin(6.28 * i/128.0));

    // now set up serial port communication with the arduino
    println("Available serial ports:");
    println(Serial.list());

    // YOU MUST REPLACE PORT 6 WITH THE CORRECT PORT FOR YOUR SETUP
    // LOOK AT THE OUTPUT TO DECIDE WHICH USB SERIAL PORT TO USE
    port = new Serial(this, Serial.list()[7],57600);
    drawFrame();
    graphData();
}

void draw() {
    port.write(65);
    delay(800);

    readData();
    drawFrame();
    graphData();
}

// Save data when mouse is clicked
void mouseClicked() {
    String[] lines = new String[256];
    String filename = String.valueOf(year());
    filename += '-' + String.format("%02d", month());
    filename += '-' + String.format("%02d", day());
    filename += '-' + String.format("%02d", hour());
    filename += '-' + String.format("%02d", minute());
    filename += '-' + String.format("%02d", second());
    filename += ".txt";

    for (int i = 0; i < 256; i++)
        lines[i] = String.valueOf(data[i]);

    saveStrings(filename, lines);
}

void readData() {
    String number;
    int i=0;
    while (port.available() > 0 && i<512) {
        bdata[i] = port.read();
        i++;
    }
    port.clear();
    for (i=0; i<256; i++)
        data[i] = bdata[2*i] + bdata[2*i+1]*256;
}

void drawFrame() {
    background(OIT_BLUE);

    // Set the left and top margin
    translate(fontsize*6, fontsize*3);

    // Rectangle that frames the graph
    stroke(OIT_YELLOW);
    strokeWeight(3);
    line(0,0,xSize,0);
    line(xSize,0,xSize,ySize);
    line(xSize,ySize,0,ySize);
    line(0,ySize,0,0);

    // Horizontal gridlines
    textAlign(RIGHT);
    for (int i=100; i<=1000; i+=100) {
        int ypos = int(ySize-i*ySize/1024);
        strokeWeight(1);
        if (i==200 || i==400 || i==600 || i==800 || i==1000) {
            strokeWeight(2);
            text(String.valueOf(i),  -fontsize/2, ypos+fontsize/3);
        }        
        line(0,ypos,xSize,ypos);
    }

    // Vertical gridlines
    fill(OIT_YELLOW);
    textAlign(CENTER);
    for (int i=-8; i<=8; i+=2) {
        if (i==0)
            strokeWeight(2);
        else
            strokeWeight(1);
        int xpos = int(xSize/2+(i*1000.0/63.5)*(xSize/256.0));
        line(xpos,0,xpos,ySize);
        text(String.valueOf(i),   xpos,       ySize+fontsize);
    }

    //  Labels
    text("** Click Mouse to Save Data to Time Stamped File **", xSize/2, -fontsize/2);
    text("Position (mm)", xSize/2, ySize+5*fontsize/2);
   
    translate(-3*fontsize, int(ySize/2));
    rotate(-PI/2.0);               // Rotate by theta
    text("Intensity (counts)",  0,0);
    rotate(PI/2.0);               // Rotate by theta
    translate(3*fontsize, -int(ySize/2));
}

void graphData() {
    stroke(255);
    for (int i=0; i<256; i++) {
        int x = i * xSize/ 256;
        int y = ySize - data[i] * ySize/1024;
        ellipse(x,y,1,2);
    }
}
