
-- psql postgres -U eating_meeting

CREATE DATABASE eating_meeting;
GRANT ALL PRIVILEGES ON DATABASE eating_meeting TO eating_meeting;

CREATE TABLE category(
   id serial PRIMARY KEY,
   name VARCHAR (50) UNIQUE NOT NULL,
   zomato_ids int []
);

INSERT INTO category VALUES (1, 'Dinner', '{1,2}');


CREATE TABLE guest(
   id serial PRIMARY KEY,
   first_name VARCHAR (50) NOT NULL,
   last_name VARCHAR (50) NOT NULL,
   email VARCHAR (50) NOT NULL
);


CREATE TABLE meeting(
   id serial PRIMARY KEY,
   restaurant_id INTEGER NOT NULL,
   date TIMESTAMP NOT NULL
);

CREATE TABLE meeting_guest(
    guest_id int,
    meeting_id int,
    CONSTRAINT FK_guest
        FOREIGN KEY (guest_id) REFERENCES guest (id),
    CONSTRAINT FK_meeting
        FOREIGN KEY (meeting_id) REFERENCES guest (id)
);
