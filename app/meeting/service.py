from .dao import meeting_dao
from app.aws.email_ses import emailing


class MeetingService(object):

    def create_meeting(self, meeting):
        # TODO check users exists
        # TODO check restaurant exists
        # TODO check future date

        meeting_dao.create(meeting)
        for g in meeting.guests:
            # TODO send emails all together
            email = emailing.build_email(g.email, g.first_name, g.last_name, meeting.date, meeting.restaurant_id)
            emailing.send_email(g.email, email)

        return meeting


meeting_service = MeetingService()
