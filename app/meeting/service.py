from .dao import meeting_dao
from .model import Meeting
from app.guest.model import Guest


class MeetingService(object):

    def create_meeting(self, meeting):
        # TODO check users exists
        # TODO check restaurant exists
        # TODO check future date

        meeting_dao.create(meeting)

        return meeting


meeting_service = MeetingService()
