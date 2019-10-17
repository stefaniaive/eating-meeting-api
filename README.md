# **eating-meeting-api**

Esta API es un prototipo para una aplicacion que permite buscar un restaurant deseado para una reunion determinada. Esta puede ser una reunion de trabajo, de amigos, romantica, o lo que se desee.
La misma permite una vez seleccionado el restaurant donde se desea llevar a cabo , crear la reunion para una fecha determinada asociada a los invitados que se quiera.
En lo implementado una vez creada la reunion se enviara un email a cada uno de los invitados informandole de la misma.

Nice to have:
- Posibilidad de crear un evento en el calendar a traves de la API de google que se adjunte al email y permita a los invitados marcar si asistiran o no a la misma, pudiendo en caso positivo agrgarla a su calendario.
- Crear alertas periodicas recordando la reunion (Email o push notifications)


Servicios publicados: 

GET https://eating-meeting-api.herokuapp.com/eating-meeting-api/categories 

> Devuelve las categorias posibles para los restaurants

GET https://eating-meeting-api.herokuapp.com/eating-meeting-api/restaurants
> Permite obtener los restaurants disponibles

Query Params permitidos:
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

> Permite crear una reunion en un restaurant determinado, en una fecha para los invitados deseados


## **Clientes**

Nodejs: https://github.com/stefaniaive/eating-meeting-nodejs-client

## **Dependencias**

- Zomato API 

> https://developers.zomato.com/documentation?lang=es_cl#!/restaurant/search

- Amazon SES

> https://aws.amazon.com/es/ses/