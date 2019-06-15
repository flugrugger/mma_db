CREATE TABLE IF NOT EXISTS fighter_stats (
	fighter_id INT NOT NULL AUTO_INCREMENT,
	name varchar(50),
	age INT,
	height_ft FLOAT,
	weight_lbs INT,
	reach_inch INT,
	gym varchar(50),
	PRIMARY KEY (fighter_id)
);

LOAD DATA INFILE 'fighter_stats.csv' 
INTO TABLE fighter_stats 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(name, age, height_ft, weight_lbs, reach_inch, gym);