from course import courses
import logging
import log.log

class ineuron:
    #constructor
    def __init__(self, instructor_name, subject):

        # protected,private
        self.__instructor_name = instructor_name
        self._subject = subject
        self.course = []

    def get_info(self):

        logging.info(f"Instructor Details --> name: {self.__instructor_name},subjects: {self._subject}")
        return (self.__instructor_name, self._subject)




    def add_courses(self, cname, fee):
        logging.info(f"New course : {cname},{fee}")
        obj = courses(cname, fee)
        #print("New Course : " , obj)

        self.course.append(obj)
        for i in self.course:
             pass
        print(i.course_info())

    def list(self):
        logging.info(f"Course list {self.course}")
        return self.course