# Automated-Door
This project presents the concept of edge services in the Internet of things on a small scale.
It consists of a combination of a motor and P-Infrared sensors.

The use case resembles the automatic door where the infrared sensor, senses the movement nearby and triggers the motor to turn on and off.
A motor chip, L293D is required to control the motor using the smart IoT platform (RPi3).

Whenever the infrared sensor is triggered (Value=1), the motor moves in a clockwise direction (Door opens) and when there's no movement (Value=0), the motor moves in an anti-clockwise direction (Door closes) for a certain time.
