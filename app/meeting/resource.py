from flask_restful import Resource
from flask import request
from .schema import meeting_schema, meeting_input_schema
from .service import meeting_service
import json


class MeetingCollectionResource(Resource):

    def post(self):
        payload =  json.dumps(request.get_json(force=True, silent=True))
        meeting_entity, errors = meeting_schema.loads(payload)

        # TODO Handle exception
        if errors:
            raise Exception

        meeting = meeting_service.create_meeting(meeting_entity)
        return json.loads(meeting_schema.dumps(meeting).data)
