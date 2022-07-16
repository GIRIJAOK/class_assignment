import logging

class courses:
    def __init__(self, course_name, fees):
        self.__course_name = course_name
        self.__fees = fees

    def course_info(self):

        logging.info(f"Course information--> Name: {self.__course_name}, Fee: {self.__fees}  ")
        return (self.__course_name, self.__fees )

