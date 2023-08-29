CREATE TABLE Users (
	id serial4 NOT NULL,
	fio varchar(255),
	birthdate date,
	sex boolean,
	description varchar,
	achievements varchar, --достижения
	education varchar,
	phoneNumber varchar(50),
	email varchar(255),
	CONSTRAINT users_pkey PRIMARY KEY (id)
);

CREATE TABLE Hobby (
	id serial4 NOT NULL,
	hobbyName varchar(255),
	CONSTRAINT hobby_pkey PRIMARY KEY (id)
);

CREATE TABLE UserHobbyList (
	id serial4 NOT NULL,
	fkUser serial4,
	fkHobby serial4,
	CONSTRAINT UserHobbyList_pkey PRIMARY KEY (id),
	CONSTRAINT UserHobbyList_fkUser_fkey FOREIGN KEY (fkUser) REFERENCES Users(id),
	CONSTRAINT UserHobbyList_fkHobby_fkey FOREIGN KEY (fkHobby) REFERENCES Hobby(id)
);

CREATE TABLE Profession (
	id serial4 NOT NULL,
	professionName varchar(255),
	CONSTRAINT Profession_pkey PRIMARY KEY (id)
);
CREATE TABLE UserProfessionList (
	id serial4 NOT NULL,
	fkUser serial4,
	fkProfession serial4,
	CONSTRAINT UserProfessionList_pkey PRIMARY KEY (id),
	CONSTRAINT UserProfessionList_fkUser_fkey FOREIGN KEY (fkUser) REFERENCES Users(id),
	CONSTRAINT UserProfessionList_fkProfession_fkey FOREIGN KEY (fkProfession) REFERENCES Profession(id)
);

CREATE TABLE Projects (
	id serial4 NOT NULL,
	projectName varchar(255),
	target varchar,
	readyState int2,
	description varchar,
	achievements varchar,
	education varchar,
	fkUserOwner serial4,
	photoLink varchar,
	presentationLink varchar, 
	CONSTRAINT Projects_pkey PRIMARY KEY (id),
	CONSTRAINT Projects_fkUserOwner_fkey FOREIGN KEY (fkUserOwner) REFERENCES Users(id)
);

CREATE TABLE Categories (
	id serial4 NOT NULL,
	categoriesName varchar(255),
	CONSTRAINT Categories_pkey PRIMARY KEY (id)
);

CREATE TABLE ProjectCategories (
	id serial4 NOT NULL,
	fkProject serial4,
	fkCategory serial4,
	CONSTRAINT ProjectCategories_pkey PRIMARY KEY (id),
	CONSTRAINT ProjectCategories_fkProject_fkey FOREIGN KEY (fkProject) REFERENCES Projects(id),
	CONSTRAINT ProjectCategories_fkCategory_fkey FOREIGN KEY (fkCategory) REFERENCES Categories(id)
);

CREATE TABLE ProjectNeedProfession (
	id serial4 NOT NULL,
	fkProject serial4,
	fkProfession serial4,
	CONSTRAINT ProjectNeedProfession_pkey PRIMARY KEY (id),
	CONSTRAINT ProjectNeedProfession_fkProject_fkey FOREIGN KEY (fkProject) REFERENCES Projects(id),
	CONSTRAINT ProjectNeedProfession_fkProfession_fkey FOREIGN KEY (fkProfession) REFERENCES Profession(id)
);

CREATE TABLE ProjectResponsies (
	id serial4 NOT NULL,
	fkProject serial4,
	fkUser serial4,
	CONSTRAINT ProjectResponsies_pkey PRIMARY KEY (id),
	CONSTRAINT ProjectResponsies_fkProject_fkey FOREIGN KEY (fkProject) REFERENCES Projects(id),
	CONSTRAINT ProjectResponsies_fkUser_fkey FOREIGN KEY (fkUser) REFERENCES Users(id)
);