
class BaseResponse:
    def __init__(
        self,
        success: bool,
        message: str,
        data: str | dict
    ) -> None:
        self.success = success
        self.message = message
        self.data = data
        
    