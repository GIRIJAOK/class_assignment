import logging

class student:

    __Reg_no = 10


    # constructor
    def __init__(self, name):

        logging.info(f"Student Name : {name}")
        self.name = name



    def no(self, Reg_No):

        logging.info(f"Register number assignment : {Reg_No}")
        self.__Reg_no = Reg_No

    def stud_info(self):
        try:
            logging.info(f"Student Name : {self.name}")
            logging.info(f"Student  Register Number: {self.__Reg_no}")
            return (self.name,self.__Reg_no)
        except Exception as e:
            logging.exception(e)