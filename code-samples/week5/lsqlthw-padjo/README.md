#Notes on Learn SQL the Hard Way and Padjo SQL Tutorial

*	Display the header and column while echoing the results:

	sqlite3 -header -column -echo mydata.db < ex09.sql

*	There should not be a comma on the final column when creating a database.
*	BEGIN, COMMIT, and ROLLBACK should also have a ; at the end.
*	There should be a BEGIN command for every rollback.
*	BEGIN, COMMIT, and ROLLBACK is the same as BEGIN TRANSACTION, COMMIT TRANSACTION, and ROLLBACK TRANSACTION respectively.


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

####Fuzzy Matching

As opposed to this:
	
	SELECT * from sfpd_incidents
	WHERE Resolution = 'ARREST, BOOKED' OR Resolution = 'ARREST, CITED'
We have:

	SELECT * from sfpd_incidents
	WHERE Resolution LIKE 'ARREST%'
	
Other examples:

prepend the wildcard. The command below will return any rows with "AGGRAVATED ASSAULT"
	
	SELECT * FROM sfpd_incidents
	WHERE Descript LIKE '%AGGRAVATED ASSAULT%'

For a hacky time and date filtering, this would select all records in which the Date took place in May:

	SELECT * from sfpd_incidents WHERE Date LIKE '%-05-%'

The underscore wildcard. the underscore, '_', can act as a stand-in for a single character. The example below will catch all records in which the proposition 'OF' or 'ON' were used.

	SELECT * FROM sfpd_incidents
	WHERE Descript LIKE 'AGGRAVATED ASSAULT O_'

####GROUP BY
This would return all entries of a given column/s without repetitions.

ex:
	
	SELECT PdDistrict FROM sfpd_incidents GROUP BY PdDistrict

This would return:

	PdDistrict
	BAYVIEW
	CENTRAL
	INGLESIDE
	MISSION
	NORTHERN
	PARK
	RICHMOND
	SOUTHERN
	TARAVAL
	TENDERLOIN

ex:

If we wanted to find the number of police districts that had at least one POLICE OFFICER incident in the year 2006, we just add to the WHERE conditions:

	SELECT PdDistrict, Descript
	FROM sfpd_incidents
	WHERE
	Descript LIKE '%POLICE OFFICER%'
	AND Date LIKE '2006%'
	GROUP BY PdDistrict, Descript

####LIMIT
Limit the returned entries

ex:

Limit the returned entries to only 5:

	SELECT IncidntNum, Date, Time
	FROM sfpd_incidents
	ORDER BY Date
	LIMIT 5

####ASC and DESC
Used with ORDER BY. By default, ORDER BY will return results in ascending order.

ex:

	SELECT IncidntNum, Date, Time
	FROM sfpd_incidents
	ORDER BY Date DESC, Time DESC
	LIMIT 5

####COUNT(1)
Returns the count of values returned by GROUP BY. COUNT(1) is the same as COUNT(*)


ex:

Show the top 3 districts when it comes to making arresting suspected stalkers.

	SELECT PdDistrict, COUNT(1) AS c 
	FROM sfpd_incidents
	WHERE 
	Descript = 'STALKING'
	AND Resolution LIKE 'ARREST%'
	GROUP BY PdDistrict
	ORDER BY c DESC
	LIMIT 3

####JOIN, ON
For joining rows from different tables. JOIN is the same as INNER JOIN

ex:

The query will connect row from three tables.

	SELECT social_accounts.twitter_screen_name, members.first_name, members.last_name, members.party, twitter_profiles followers_count, twitter_profiles.statuses_count, twitter_profiles.created_at
	FROM members
	JOIN social_accounts
	ON social_accounts.bioguide_id = members.bioguide_id
	JOIN twitter_profiles
	ON twitter_profiles.screen_name = social_accounts.twitter_screen_name

####HAVING
Its like WHERE but normally used on COUNT

ex:

Query below is to find all current Congressmembers who are now senators but had been representatives:

	SELECT members.first_name, members.last_name, members.current_role, COUNT(*) as diff_term_count 
	FROM members
	INNER JOIN terms
	WHERE
	members.bioguide_id = terms.bioguide_id
	AND
	members.current_role != terms.role
	AND
	members.current_role = 'sen'
	GROUP BY
	members.bioguide_id
	HAVING diff_term_count >= 1
