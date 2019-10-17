from db.postgress_connector import db

class MeetingDAO(object):

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()

        return entity

meeting_dao = MeetingDAO()
