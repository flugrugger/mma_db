CREATE TABLE IF NOT EXISTS fights_watched (
	watch_id INT NOT NULL AUTO_INCREMENT,
	date_watched TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	fighter_1 varchar(50),
	fighter_2 varchar(50),
	fight_number INT DEFAULT 1,
	promotion varchar(50) DEFAULT 'UFC',
	weight varchar(50),
	PRIMARY KEY (watch_id)
);

