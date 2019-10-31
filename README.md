# **eating-meeting-api**

This API is a prototype for an application that allows to search for an specific restaurant to creaate a meeting. This could be a meeting of bussiness, friends, or anything else.
This application allows to search and select a restauarant at first, and then the guests who will receive the invitations by email. 

Nice to have:
- Add functionality to create a calendar event with google API, to attach it to the email, allowing guest to accept or not the invitation and adding it to their personal calendars.
- Create reminders for the meeting ( by email or push notifications)

Published services: 

GET https://eating-meeting-api.herokuapp.com/eating-meeting-api/categories 

> Return the restaurant categories

GET https://eating-meeting-api.herokuapp.com/eating-meeting-api/restaurants
> Return the restaurants by filters

Query Params Required:
city_id, category_id


POST https://eating-meeting-api.herokuapp.com/eating-meeting-api/meetings

{

	"restaurant_id": "<id-restaurant>",
	
	"date": "2019-11-11T17:50:06",
	
	"guests": [{
		"first_name": "Maria",
		"last_name": "Perez",
		"email": "mariaperez@test.com"
	}]
}

> Create a new meeting for a restaurant, date and guests

## **Clients**

Nodejs: https://github.com/stefaniaive/eating-meeting-nodejs-client

## **Dependencies**

- Zomato API 

> https://developers.zomato.com/documentation?lang=es_cl#!/restaurant/search

- Amazon SES

> https://aws.amazon.com/es/ses/

## **Tools**

- Python 3
- Flask
- Postgres SQL