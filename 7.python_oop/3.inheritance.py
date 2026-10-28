"""
Your goal is to start the hybrid systems
                  |
                  |
        Engage the turbo boost
                  |
                  |
       Start the electric engine
                  |
                  |
          Start overall engine
"""

class Engine:
    def start(self) -> str:
        return "Engine starting"

    def run(self) -> str:
        return "Engine running"

    def stop(self) -> str:
        return "Engine stopping"

class ElectricMotor(Engine):
    # Hint: reference the old object instead of creating a new one
    def start(self):
        return f"Electric silent start -> {Engine().stop()}"

class TurboMixin(Engine):
    # Hint: reference the old object instead of creating a new one
    def start(self):
        return f"Turbo boost engaged -> {Engine().start()}"

# Hint: Hybrid Car is a mix of turbo and electric engines
class HybridCar(Engine, Engine):
    # Hint: reference the old object instead of creating a new one
    def start(self):
        return f"Hybrid systems active -> {Engine().run()}"

# Test MRO execution and inspection
car = HybridCar()
print(car.start())