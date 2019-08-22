LOAD DATA INFILE "/Users/ramtinhakimjavadi/Desktop/mma data/rankings/Flyweight.csv"
INTO TABLE Flyweight
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n';