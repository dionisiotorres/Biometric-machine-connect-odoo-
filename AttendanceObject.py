
class attendanceObjects:
    def __init__(self,_user_id,_timestamp):
        self.user_id=_user_id
        self.timestamp=_timestamp

    def get_userId(self):
        return self.user_id

    def get_timestamp(self):
        return self.timestamp

    def set_userId(self,user_id):
        self.user_id=user_id

    def set_timestamp(self,timestamp):
        self.timestamp=timestamp
