rm rankings/all.csv

echo ""
echo "***Old csv file deleted***"
echo ""

python scrape_rankings.py

echo ""
echo "***New data has been scraped from UFC website***"
echo ""

mysql -uroot -e"use mma; delete from UFC_rankings; LOAD DATA INFILE '/Users/ramtinhakimjavadi/Desktop/mma data/getting_UFC_rankings/rankings/all.csv' INTO TABLE UFC_rankings  COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' ESCAPED BY '\"' LINES TERMINATED BY '\n' (weight_class, fighter_name, ranking);"

echo ""
echo "***The UFC rankings have been updated on the MySQL database***"
echo ""
