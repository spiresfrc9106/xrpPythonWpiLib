from commands.arcadeDrive import ArcadeDrive
import wpilib
import wpilib.drive
import wpilib.interfaces
import commands2
import xrp

class Drivetrain(commands2.SubsystemBase):
    def __init__(self):
      super().__init__()

      self.leftFront = xrp.XRPMotor(0)
      self.rightFront = xrp.XRPMotor(1)

      self.driver = wpilib.drive.DifferentialDrive(self.leftFront, self.rightFront)

      self.gyro = xrp.XRPGyro()

    def drive(self, xaxisSpeed, zaxisRotate):
       self.arcadeDrive(xaxisSpeed, zaxisRotate)

    def arcadeDrive(self, xaxisSpeed: float, zaxisRotate: float):
       self.driver.arcadeDrive(xaxisSpeed, zaxisRotate, False ) 

    def setSlowMaxOutput(self, speed: float):
       pass
        
    def setNormalMaxOutput(self, speed: float):
       pass
    

