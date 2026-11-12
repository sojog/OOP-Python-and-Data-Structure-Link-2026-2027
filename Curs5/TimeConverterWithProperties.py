class TimeConverter: # CamelCase
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes

    def __str__(self):
        return f"{self.__hours} ore si {self.__minutes} minute"

    def __repr__(self):
        return self.__str__()

    @property
    def to_minutes(self):
        return self.__hours * 60 + self.__minutes

    @property
    def to_hours(self):
        return self.__hours + self.__minutes / 60


    # t1 + t2
    def __add__(self, other):
        total_minutes = self.to_minutes + other.to_minutes
        return TimeConverter(total_minutes // 60, total_minutes % 60)


    def __sub__(self, other):
        total_minutes = abs(self.to_minutes - other.to_minutes)
        return TimeConverter(total_minutes // 60, total_minutes % 60)

    # t1 = t1 + t2
    # def __iadd__(self, other):
    #     pass