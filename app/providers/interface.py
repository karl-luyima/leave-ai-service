from abc import ABC, abstractmethod



class LeaveDataProvider(ABC):


    @abstractmethod
    def get_employee(
        self,
        employee_id=None
    ):
        pass



    @abstractmethod
    def get_leave_history(
        self,
        employee_id=None
    ):
        pass



    @abstractmethod
    def get_leave_requests(
        self,
        employee_id=None
    ):
        pass



    @abstractmethod
    def get_leave_types(
        self
    ):
        pass



    @abstractmethod
    def get_policy(
        self
    ):
        pass