import commands2
import wpilib

class autonomous(commands2.CommandBase):
    def __init__(self, drivetrain, controller):
       super().__init__()
       self.drivetrain = drivetrain
       self.controller = controller

       self.timer = wpilib.Timer()
       self.timer.start()

       self.addRequirements(self.drivetrain)

    def execute(self) -> None:
        self.drivetrain.drive(0, -0.6)

    def end(self, interrupted: bool):
        self.drivetrain.drive(0,0)
        
    def isFinished(self) -> bool:
        return self.timer.get() > 2
