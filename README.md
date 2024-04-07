# xrpPythonWpiLib

This repo python source code based upon [RobotPy](https://robotpy.github.io/docs/) - [RobotPy at readthedocs.io](https://robotpy.readthedocs.io/en/stable/) -
code for the [XRP](https://experientialrobotics.org/). 

Robotpy add a Python programming environment to the [WPILib](https://docs.wpilib.org/en/stable/) software
development environment for [FRC](https://www.firstinspires.org/robotics/frc) robots, for Python development. Prior to robotpy, FRC
robots were programmed in C++ or Java.

## TL;DR

For those in the "too long; didn't read" camp, here are the steps to get Python program, using RobotPy and WPILib,
controlling an XRP.  These instructions are for a Windows PC, but similar steps should work on a Linux computer or
a Mac.


### Steps

* [Download and install wpilib](https://github.com/wpilibsuite/allwpilib/releases) - TODO need to verify this step is needed with RobotPy
* Follow **some** of the steps in https://docs.wpilib.org/en/stable/docs/xrp-robot/hardware-and-imaging.html and https://xrpusersguide.readthedocs.io/en/latest/course/building.html
  * Note 1: If you follow the complete video, it uses [XRP Code from WPI (https://xrpcode.wpi.edu/)](https://xrpcode.wpi.edu/) 
    to test out the robot build. Which is a different development environment than
    the [FRC Control System](https://docs.wpilib.org/en/stable/) development environment firmware that these steps
    load into the XRP.
  * Note 2: Follow the [steps](https://docs.wpilib.org/en/stable/docs/xrp-robot/index.html#getting-started-with-xrp):
    * Getting Started with XRP
      * XRP Hardware, Assembly and Imaging
      * Getting to know your XRP
      * XRP Hardware Support
      * The XRP Web UI
      * But stop before "Programming the XRP"
* Make sure your computer is reconnected to the internet and not your XRP
* [Download and install Python 3.12](https://www.python.org/downloads/release/python-3122/)
* Download this repo from https://github.com/spiresfrc9106/xrpPythonWpiLib
  * If you downloaded as a zip file, unzip into a directory
  * Open a Windows PowerShell Window
    * Because RobotPy uses the `pyproject.toml` that is in `xrpPythonWpiLib` the Change directory (cd) to the directory where you downloaded and perhaps unzip `xrpPythonWpiLib`:
       ```commandline
       cd C:\Users\MikeStitt\Documents\first\sw\xrpPythonWpiLib
       pwd
    
       Path
       ----
       C:\Users\MikeStitt\Documents\first\sw\xrpPythonWpiLib
       ```
    * Verify that your Python command is python 
       ```commandline
       python -VV
       Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]
       ```
    * Install RobotPy
      ```commandline
      python -m pip install --upgrade pip
      python -m pip install robotpy
      ```
    * From the `xrpPythonWpiLib` directory, do a RobotPy sync:
      ```commandline
      python -m robotpy sync
      10:46:36:743 INFO    : robotpy.installer   : RobotPy Installer 2024.2.2
      10:46:36:744 INFO    : robotpy.installer   : -> caching files at C:\Users\MikeStitt\wpilib\2024\robotpy
      10:46:36:756 INFO    : sync                : RobotPy version in `pyproject.toml` is '2024.3.2.1'
      10:46:37:078 INFO    : sync                : Latest version of RobotPy is '2024.3.2.1'
      10:46:37:083 INFO    : sync                : Robot project requirements:
      10:46:37:083 INFO    : sync                : - robotpy[commands2,xrp]==2024.3.2.1
      10:46:37:083 INFO    : sync                : Downloading Python for RoboRIO
  
      <- SNIP ->
  
      pip is launching in a new window to complete the installation
      ```
  * Connect a **wired-only USB** xbox controller to your PC. This can be confusing because some xbox controllers have
    a USB connector for charging, but are **wireless** xbox controller. These will not work. Logitech xbox controllers
    will work, if the switch on the back of them are switched to the "X" mode using the  "X" or "D" switch on the back
    of the controller.
  * Powerup the XRP
  * Connect to the XRP WiFi network
  * Go back to your Windows PowerShell Window.
    * This step can be confusing for those that know how to simulate and deploy to full-sized FRC robots. Use RobotPy to
      launch the WPILib simulator to control the XRP from the Windows PowerShell that is in the `xrpPythonWpiLib` directory:
      ```commandline
      python -m robotpy sim --xrp
      ```
      resulting in:
      ```commandline
      11:16:58:836 INFO    : halsim_gui          : WPILib HAL Simulation 2024.3.2.0
      HAL Extensions: Attempting to load: halsim_gui
      Simulator GUI Initializing.
      Simulator GUI Initialized!
      HAL Extensions: Successfully loaded extension
      11:16:59:364 INFO    : xrp.extension       : WPILib XRP client 2024.3.2.0
      HAL Extensions: Attempting to load: halsim_xrp
      HALSim XRP Extension Initializing
      HALSimXRP Initialized
      HALSim XRP Extension Initialized
      HAL Extensions: Successfully loaded extension
      11:16:59:393 WARNING : pyfrc.physics       : Cannot enable physics support, C:\Users\MikeStitt\Documents\first\sw\xrp_python_minimal\physics.py not found
      11:16:59:394 INFO    : wpilib              : RobotPy version 2024.3.2.1
      11:16:59:394 INFO    : wpilib              : WPILib version 2024.3.2.0
      11:16:59:395 INFO    : wpilib              : Running with simulated HAL.
      11:16:59:402 INFO    : nt                  : Listening on NT3 port 1735, NT4 port 5810
      Not loading CameraServerShared
    
      ********** Robot program startup complete **********
      Default frc::IterativeRobotBase::RobotPeriodic() method... Override me!
      Default frc::IterativeRobotBase::SimulationPeriodic() method... Override me!
      ```
      and a "Robot Simulation" window appearing. (TODO add an image of the "Robot Simulation" window.)
  * In the "Robot Simulation", from the "System Joysticks" window, drag and drop "0: Xbox Controller" to the "Joysticks" window, "Joystick[0]" column header.
  * In the "Robot Simulation", in the "Robot Stat" window, select "Teleoperated".
  * Drive your XRP around with your xbox controller joysticks. TODO, on a Logitech controller the rotate left and right is backwards.


## Thanks, Tom!

This software is based upon the FRC2024.zip file from Tom Corrigan, of FRC5878, published here: https://www.chiefdelphi.com/t/using-robotpy-with-xrp/452186/18

From Tom: "Here’s my code. Do with what you will." ;-)

Thanks, Tom! - Mike


## Why XRP?

Learning to develop programs to control a full size, 100 pound, [FRC](https://www.firstinspires.org/robotics/frc)
competition robot can be scary and expensive. Care and attention is needed to keep a 100 pound robot with a
battery capable of more than a kilowatt of power safe.

The XRP scales the problem down to a robot 1/100th the size, reducing the care and attention needed to stay safe.

While it is small, the XPR still has the angular rate gyros, the accelerometers, the line following sensors, 
and the ultrasonic ranging finding sensors needed to learn about programing robot closed loop control systems.
Systems where the software uses the feedback from the sensor input to actively control the robot.


## XRP or Romi

The [XRP](https://experientialrobotics.org/) is similar, but different from the [Romi](https://docs.wpilib.org/en/stable/docs/romi-robot/index.html).


## Background on XRP Software Development Environments

There are at least two different XRP software development environments, each with different firmware
loaded into the XRP.

1. A micropython development environment - using [XRP Code from WPI - https://xrpcode.wpi.edu/](https://xrpcode.wpi.edu/)
2. A [FRC](https://www.firstinspires.org/robotics/frc) development environment for
[FRC Control System](https://docs.wpilib.org/en/stable/) - using
[XRP WPILib Firmware](https://github.com/wpilibsuite/xrp-wpilib-firmware/releases)

Only one of the these software development environments will be loaded onto your XRP at a time.

If you go to https://xrpcode.wpi.edu/ in a web browser and try to connect to an XRP and the micropython development
environment firmware is not installed on the XRP, perhaps because the XRP left the factory unprogrammed, or because 
[XRP WPILib Firmware](https://github.com/wpilibsuite/xrp-wpilib-firmware/releases) is programmed onto the XRP, 
the https://xrpcode.wpi.edu/ website will, eventually prompt you
through the steps to re-install the micropython development environment. If you had the xrp-wpilib-firmware installed,
it will be over-written with the micropython development environment firmware.

The website https://docs.wpilib.org/en/stable/docs/xrp-robot/hardware-and-imaging.html desribes the steps to replace
the micropython development environment firmware with 
[XRP WPILib Firmware](https://github.com/wpilibsuite/xrp-wpilib-firmware/releases).

One can reconfigure a XRP back and forth between https://xrpcode.wpi.edu/ based firmware and
[XRP WPILib Firmware](https://github.com/wpilibsuite/xrp-wpilib-firmware/releases).

This example uses the [FRC Control System](https://docs.wpilib.org/en/stable/) development environment.


## LabVIEW, C++, Java, and Python

The [FRC Control System](https://docs.wpilib.org/en/stable/) development environment supports coding in 
[National Instruments LabView](https://learn.ni.com/learn/article/labview-tutorial),
[C++](https://en.wikipedia.org/wiki/C%2B%2B), [Java](https://en.wikipedia.org/wiki/Java_(programming_language)),
and [Python](https://en.wikipedia.org/wiki/Python_(programming_language)).

See [WPILib VS Code Overview](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/index.html), WPILib
VS Code is a special version of 
[Microsoft Visual Studio Code](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/index.html), which
is different than [Microsoft Visual Studio](https://visualstudio.microsoft.com/).
For C++ and Java development, WPILib VS Code is used to create project templates and example projects,
write the source code, start the simulator, and to launch a deployment of the code to a robot.

For Python, RobotPy based WPILib development, one can use any editor to write the code, and then a terminal window, e.g.


## Why Python for FRC?

The main advantages of Python for FRC:
- It is taught in high school AP computer science
- In 2024, Students are more likely to use Python in college or their careers than C++ or Java
- It is easier to lear with less syntaxic constraints than C++ or Java
- Python programs are smaller making them more accessible to beginning programmers

The main disadvantage is that it [duck typed](https://en.wikipedia.org/wiki/Duck_typing) leading to bugs that are not
found at compile time unlike [weakly and strongly typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing)
languages such as C++ or Java.

Linting, unit testing, and simulation should be used to overcome the [duck typed](https://en.wikipedia.org/wiki/Duck_typing)
disadvantage of Python.


## FRC Control System for XRP and Romi Simulation Weirdness

Normally, when using the [FRC Control System](https://docs.wpilib.org/en/stable/) one has the option to run the
simulator which runs your robot
code within a simulation of a robot within your computer. For full sized 
[roboRIO](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-introduction.html) base robots. This
simulation is **totally** different than deploying your program to the roboRIO and running it on a real powered up
robot.

But for [XRP](https://experientialrobotics.org/) and
[Romi](https://docs.wpilib.org/en/stable/docs/romi-robot/index.html), this line between the running the simulator 
and deploying on a physical robot is blurred.

This can cause confusion when figuring out how to get started with the XRP and RobotPy.

See: https://docs.wpilib.org/en/stable/docs/romi-robot/programming-romi.html


> One aspect where a Romi project differs from a regular FRC robot project is that the code is not deployed directly 
> to the Romi. Instead, a Romi project runs on your development computer and leverages the WPILib simulation framework
> to communicate with the Romi robot.

If you've never loaded code into a roboRIO on a real robot or simulated robot code on a PC, you can safely ignore the
rest of this section. But if you have, you might want to review running a program to control a Romi or XRP is different
from a full sized roboRIO based robot.

For the XRP and Python, we'll do something a little different than these C++ and Java instructions for the Romi and 
the [FRC Control System](https://docs.wpilib.org/en/stable/), but they are reposted here for background context
(don't do these steps):

> To run a Romi program, first, ensure that your Romi is powered on. Next, connect to the WPILibPi-<number> WiFi
> network broadcast by the Romi. If you changed the Romi network settings (for example, to connect it to your own 
> WiFi network) you may change the IP address that your program uses to connect to the Romi. To do this, open 
> the build.gradle file and update the wpi.sim.envVar line to the appropriate IP address.


An example WPILib Java or C++ for Romi build.gradle file:
```
//Sets the websocket client remote host.
wpi.sim.envVar("HALSIMWS_HOST", "10.0.0.2")
wpi.sim.addWebsocketsServer().defaultEnabled = true
wpi.sim.addWebsocketsClient().defaultEnabled = true
```

More instructions from https://docs.wpilib.org/en/stable/docs/romi-robot/programming-romi.html:

> Now to start your Romi robot code, open the WPILib Command Palette (type Ctrl+Shift+P) and select “Simulate Robot Code”, or press F5.
> 
> If all goes well, you should see a line in the console output that reads “HALSimWS: WebSocket Connected”
> 
> Your Romi code is now running!

But again, the above is background information, we'll do these steps slightly different on the XRP with Python.

## Background materials

* https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html
   * https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/index.htmlhttps://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/index.html
      * https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html
      * https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html
      * https://docs.wpilib.org/en/stable/docs/xrp-robot
