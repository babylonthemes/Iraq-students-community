
class ModelRelatedNameError(Exception):
    
    def __init__(self,name) -> None:
        message = f" اسم التطبيق {name}  لا يطابق الاسم المخصص لهذا الاجرا  "
        super().__init__()