CREATE DATABASE IF NOT EXISTS got;
USE got;

CREATE TABLE IF NOT EXISTS characters (id int not null, name text not null, gender text, culture text, titles text, aliases text, born text, died text, father int, mother int, spouse int, children text, books text, primary key (id));

CREATE TABLE IF NOT EXISTS houses(id int not null, name text not null, places text, region text, coat_of_arms text, words text, founder text, current_lord text, heir text, ancestral_weapons text, primary key (id));

CREATE TABLE IF NOT EXISTS books(id int not null, name varchar(255) not null, pages int not null, preceded_by int, followed_by int, release_date date,  primary key (id));
