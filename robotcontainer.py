# from subsystems.elevator import Elevator
import wpilib
import wpilib.drive
import commands2
import commands2.button
from subsystems.drivetrain import Drivetrain
from commands.arcadeDrive import ArcadeDrive
from commands.autonomous import autonomous

class RobotContainer:
    def __init__(self) -> None:
        self.controller = commands2.button.CommandXboxController(0)   
        self.drivetrain = Drivetrain()

        self.drivetrain.setDefaultCommand(self.getArcadeDriveCommand())
        self.configureButtons()

    def getAutonomousCommand(self):
        return autonomous(self.drivetrain,self.controller)
    
    def getArcadeDriveCommand(self):
        return ArcadeDrive(self.drivetrain, self.controller)
    
    def configureButtons(self):
        """Configure the buttons for the driver's controller"""
        pass