
-- psql postgres -U eating_meeting

CREATE DATABASE eating_meeting;
GRANT ALL PRIVILEGES ON DATABASE eating_meeting TO eating_meeting;

CREATE TABLE category(
   id serial PRIMARY KEY,
   name VARCHAR (50) UNIQUE NOT NULL,
   zomato_ids int []
);

INSERT INTO category VALUES (1, 'Dinner', '{1,2}');