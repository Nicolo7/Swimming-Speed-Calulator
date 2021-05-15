# Swimming-Speed-Calulator

** PROJECT DESCRIPTION **
Using a load cell and the HX711, I want to calculate force being produced by swimmer and translate it into some velocity. This is based off the physics principle that Force = Mass * Acceleration. If force can be calculated, and mass is given by the weight of the swimmer, then the acceleration contains the velocity of the swimmer at the given instance. Other forces and variables are still at play, but starting off with that simple truth and further expanding on it will allow me to get closer to what I want. Any comments or suggestions is appreciated, this is also my first project on GitHub.

** PROJECT APPROACH **
Attempting a light weight solution, I opted for the raspberry pi zero W. The project will be written in Python and will make use of another Github Repository by underdoeg. Further credits to him can be found in the original cloned repository found in the project. This repo has a method of communication with the HX711 chip which translates the pulling forces of the load cell into a format that the raspberry pi zero can understand. Using this and some tweaking to their code, I plan on translating the data into force and using it to calculate the velocity of a swimmer.
