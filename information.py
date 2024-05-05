
class Information():

    def __init__(self) -> None:
        self.points = 0
        self.distance = 0
        self.start_distance = 0
        self.current_distance = 0
        self.min_distance = 0

    def reset_points(self):
        self.points = 0

    def reset_distance(self):
        self.distance = 0

    def print_results(self):
        print(f'Points: {self.points}')
        print(f'Distance made: {self.distance}')
        print(f'Mininum distance: {self.min_distance}')
        print(f'Current distance: {self.current_distance}')

    def reset_min_distance(self):
        self.min_distance = 0
      