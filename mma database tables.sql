CREATE TABLE IF NOT EXISTS `fights` (
	fight_id INT NOT NULL AUTO_INCREMENT,
	fighter_1 varchar(50),
	fighter_2 varchar(50),
	fight_number INT DEFAULT 1,
	weight_class varchar(50),
	duration FLOAT(2),
	method varchar(50),
	event_name varchar(50),
	event_date TIMESTAMP,
	promotion varchar(50) DEFAULT 'UFC',
	PRIMARY KEY (fight_id),
	FOREIGN KEY (fighter_1) REFERENCES fighter(full_name) ON DELETE RESTRICT,
	FOREIGN KEY (event_name) REFERENCES events(name) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS `fights_watched` (
	watch_id INT NOT NULL,
	date_watched TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	fighter_1 varchar(50),
	fighter_2 varchar(50),
	fight_number INT DEFAULT 1,
	PRIMARY KEY (watch_id),
	FOREIGN KEY (watch_id) REFERENCES fights(fight_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS `fighter` (
	fighter_id INT NOT NULL AUTO_INCREMENT,
	full_name varchar(50) UNIQUE,
	age INT,
	height_ft FLOAT,
	weight_lbs INT,
	reach_inch INT,
	gym varchar(50),
	wins INT,
	losses INT,
	PRIMARY KEY (fighter_id)
);

CREATE TABLE IF NOT EXISTS `events` (
	name varchar(50),
	promotion varchar(50),
	event_date TIMESTAMP,
	location varchar(50),
	PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS `UFC_rankings` (
	weight_class varchar(50),
	fighter_name varchar(50),
	ranking int,
	last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (weight_class, fighter_name)
);
