#Notes on Learn SQL the Hard Way and Padjo SQL Tutorial

Display the header and column while echoing the results:

	sqlite3 -header -column -echo mydata.db < ex09.sql
 
##SQL Commands
####INSERT INTO
to insert data in the database

ex:

	INSERT INTO person (id, first_name, last_name, age) VALUES (0, "Anton", "Ortiz", 25);

####REPLACE INTO
to replace the record but keep the unique id

ex:

	REPLACE INTO person (id, first_name, last_name, age) VALUES (0, 'Zed', 'Shaw', 37);

####DROP TABLE
to drop table

ex:

	DROP TABLE IF EXISTS person;
	DROP TABLE person;

####ALTER TABLE
to alter the tables

ex:

	ALTER TABLE peoples ADD COLUMN hatred INTEGER;
	ALTER TABLE peoples RENAME TO person;

####On quering entries from a given date range

ex:

    /*query entries with dates between 2004 and 2005./
    SELECT * from sfpd_incidents WHERE Date >= '2004' AND Date < '2005'
