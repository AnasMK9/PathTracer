# PathTracer
This repository contains an implementation of an indoor Wi-Fi localization algorithm to track the path of a moving transmitter called path tracer.
It was part of a research paper for my Wireless Communication course in Jordan University of Science & Technology
The paper was written in the IEEE conference paper format. 

everything in this repository except for the dependencies is mine and my team's work, so ALL copyrights are reserved.

# Files Description

1- Run.py: Runs a simulation for the algorithm and shows the real path and estimated path of movement.

2- rogueAP.py: Simulates the movement of the transmitter and stores the movement in a file.

3- server.py: A local server that receives the RSSI readings from the 4 receivers and runs the algorithm to estimate the path.

4- results.py: Refine the estimated path and produce a plot showing the real and estimated path.

