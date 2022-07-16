# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from student import student
from ineuron import ineuron

import logging
import log.log
from jobinfo import jobs
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#constructor
if __name__ == '__main__':
    print_hi('PyCharm')

    logging.info("Student Details")

    stud = student("Girija O K")
    print("Student details : ", stud.stud_info())
    stud.no(100)
    print("Student details after assignment :", stud.stud_info())



    try:
        logging.info("Instructors")
        obj = ineuron("Krish","Data Analytics")
        obj1 = ineuron("Sudhanshu", "Data Science")
        print("Instructor-1 Details:", obj.get_info())
        print("Instructor-2 Details:", obj1.get_info())
        #print(obj.list())
        obj.add_courses("Full stack FSDA" , 4000)
        obj.add_courses("Full stack FSDS", 1700)
        obj.add_courses("Full stack JAVA", 1500)
        print( obj.list())

    except Exception as e:
        logging.exception(e)


    logging.info("Job Information")
    job = jobs("Sam","Data Analys",40000)
    logging.info(f"Job Information: {job}")
    print(job.info_job())


