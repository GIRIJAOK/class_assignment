import logging

class jobs:
    # constructor
    def __init__(self, employee_name, job_title,salary):
        self._employee_name = employee_name
        self.job_title = job_title
        self.__salary = salary

    def info_job(self):
        """ Job  Information"""
        try:
            logging.info(f"Information about the job: Employee Name: {self._employee_name} , Job Title : {self.job_title} , Salary : {self.__salary}")
            return(self._employee_name,self.job_title,self.__salary)
        except Exception as e :
            logging.info(e)





