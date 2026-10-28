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
           Start the engine
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
        return f"Electric silent start -> {super().start()}"

class TurboMixin(Engine):
    # Hint: reference the old object instead of creating a new one
    def start(self):
        return f"Turbo boost engaged -> {super().start()}"

class HybridCar(ElectricMotor, TurboMixin):
    # Hint: reference the old object instead of creating a new one
    def start(self):
        return f"Hybrid systems active -> {super().start()}"

car = HybridCar()
print(car.start())