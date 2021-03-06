import sched, time

class Firefly:
    stages_per_change = 5

    def __init__(self, x, y, scheduler):
        self.stage = 0
        self.coords = (x, y)
        self.flashing = False
        self.can_flash = True
        self.scheduler = scheduler

    def flash(self, timeout, cooldown):
        if not self.can_flash: return
        # print("Flashing " + self.get_coords_str())
        self.can_flash = False
        self.flashing = True
        def stop_flashing(): self.flashing = False
        def end_cooldown(): self.can_flash = True
        self.scheduler.enter(timeout, 1, stop_flashing)
        self.scheduler.enter(cooldown, 1, end_cooldown)

    def get_curr_intensity(self) -> float:
        return self.stage / self.stages_per_change

    def tick(self):
        if not self.flashing and self.stage > 0:
            self.stage -= 1
        elif self.flashing and self.stage < self.stages_per_change:
            self.stage += 1

    def get_coords_str(self):
        return str(self.coords[0]) + ", " + str(self.coords[1])
# def print_time():
#     print(int(time.time()))
#
# s = sched.scheduler(time.time, time.sleep)
# for i in range(1, 10):
#     for j in range(1, 20):
#         s.enter(i * 2, 2, print_time)
#
# s.run()
