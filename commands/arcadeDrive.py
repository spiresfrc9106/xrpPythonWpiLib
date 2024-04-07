import wpilib
import commands2

class ArcadeDrive(commands2.CommandBase):
    def __init__(self, drivetrain, controller):
        super().__init__()
        
        self.drivetrain = drivetrain
        self.controller = controller
        self.addRequirements(self.drivetrain)
              
    def execute(self):
        self.drivetrain.arcadeDrive(-self.controller.getRawAxis(4), self.controller.getRawAxis(1))
              
    def end(self, interrupted: bool):
        self.drivetrain.drive(0,0)
        
    def isFinished(self):
        return False
    