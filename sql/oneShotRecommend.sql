
USE `cs411`;
DROP procedure IF EXISTS `cs411`.`oneShotRecommend`;

DELIMITER $$
USE `cs411`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `oneShotRecommend`(IN UserId INT)
BEGIN
-- this part find buddy with same schedule
BEGIN
DECLARE sp_TrailID INT;
DECLARE sp_Date DATE;
DECLARE exit_flag BOOLEAN DEFAULT FALSE;
DECLARE scheduleCur CURSOR FOR (
                                SELECT  TrailID, Schedule.Date
                                FROM Schedule 
                                WHERE Schedule.UserID = UserId AND Schedule.status = 'FALSE'); -- return all the trails that need to match
DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_flag = True;                                

DROP TABLE IF EXISTS matchBuddy;
CREATE TABLE matchBuddy(
Trail_name VARCHAR(150), Buddy_name VARCHAR(150), Email VARCHAR(255), Phone CHAR(10), Trail_id INT);

OPEN scheduleCur;
    Cloop: LOOP
        FETCH scheduleCur INTO sp_TrailID, sp_Date;    
        
        IF sp_TrailID = NULL THEN
            LEAVE cloop;
        ELSEIF exit_flag THEN
            LEAVE cloop;
		END IF;
        
        IF sp_Date >= CURDATE() THEN
			INSERT INTO matchBuddy (Trail_name, Buddy_name, Email, Phone, Trail_id)
				SELECT t.TrailName, au.first_name, au.email, au.Phone , t.TrailID
				FROM Schedule s NATURAL JOIN TrailInformation t JOIN auth_user au ON s.UserID = au.id
				WHERE t.TrailID = sp_TrailID AND s.DATE = sp_Date AND s.UserID != UserId AND
                s.UserID IN (SELECT sc.UserID FROM Schedule sc WHERE sc.status = 'TRUE' GROUP BY sc.UserID HAVING COUNT(*) > 1);
		END IF;
     END LOOP cloop;                           
CLOSE scheduleCur;
END;

-- this part recommend restaurtant for each trail
BEGIN
DECLARE re_TrailID INT;
DECLARE sp_Date DATE;
DECLARE day_name VARCHAR(10);
#DECLARE totcredit INT;
-- DECLARE avgPrice REAL;
DECLARE exit_flag BOOLEAN DEFAULT FALSE;
DECLARE restCur CURSOR FOR (
							SELECT  Trail_id
							FROM matchBuddy); -- return all trail id to find restaurant
DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_flag = True; 

DROP TABLE IF EXISTS matchRestaurant;
CREATE TABLE matchRestaurant(
Trail_id INT, Trail_name VARCHAR(150), Rest_id INT, RestaurantName VARCHAR(100), Address VARCHAR(255), City VARCHAR(50), State CHAR(2), PostalCode INT(5), Openhour VARCHAR(10), Closehour VARCHAR(10), Rating DECIMAL(2,1), distance_in_miles FLOAT);

-- SET day_name = CONCAT('$.', substring(DAYNAME(CURDATE()), 1, 3));
-- SELECT dayname;
OPEN restCur;
    Cloop: LOOP
        FETCH restCur INTO re_TrailID;    
        IF re_TrailID = NULL THEN
            LEAVE cloop;
        ELSEIF exit_flag THEN
            LEAVE cloop;
		END IF;
        
		INSERT INTO matchRestaurant (Trail_id, Trail_name, Rest_id, RestaurantName, Address, City, State, PostalCode, Rating, distance_in_miles, Openhour, Closehour)
		SELECT near.TrailID, near.TrailName, re.RestaurantID, re.RestaurantName, re.Address, re.City, re.State, re.PostalCode, re.Rating, near.distance_in_miles,
				CASE DAYNAME(CURDATE())
					WHEN 'Monday' THEN re.OpenHours -> '$.Mon'
                    WHEN 'Tuesday' THEN re.OpenHours -> '$.Tue'
                    WHEN 'Wednesday' THEN re.OpenHours -> '$.Wed'
                    WHEN 'Tursday' THEN re.OpenHours -> '$.Tur'
                    WHEN 'Friday' THEN re.OpenHours -> '$.Fri'
                    WHEN 'Saturday' THEN re.OpenHours -> '$.Sat'
						ELSE re.OpenHours -> '$.Sun'
                        END AS Openhour,
				CASE DAYNAME(CURDATE())
					WHEN 'Monday' THEN re.CloseHours -> '$.Mon'
                    WHEN 'Tuesday' THEN re.CloseHours -> '$.Tue'
                    WHEN 'Wednesday' THEN re.CloseHours -> '$.Wed'
                    WHEN 'Tursday' THEN re.CloseHours -> '$.Tur'
                    WHEN 'Friday' THEN re.CloseHours -> '$.Fri'
                    WHEN 'Saturday' THEN re.CloseHours -> '$.Sat'
						ELSE re.CloseHours -> '$.Sun'
                        END AS Closehour
        FROM Restaurant re NATURAL JOIN
			(SELECT *
			FROM (
					SELECT a.TrailID, a.TrailName, b.RestaurantID,
					   69 *
						DEGREES(ACOS(LEAST(1.0, COS(RADIANS(a.Latitude))
							 * COS(RADIANS(b.Latitude))
							 * COS(RADIANS(a.Longitude - b.Longitude))
							 + SIN(RADIANS(a.Latitude))
							 * SIN(RADIANS(b.Latitude))))) AS distance_in_miles
					FROM TrailInformation AS a, Restaurant AS b 
					WHERE  a.State = b.state AND a.TrailID = re_TrailID) AS dis
			ORDER BY distance_in_miles
			LIMIT 5) AS near;
		
     END LOOP cloop;                           
CLOSE restCur;
END;

-- this part will suggest buddies with there preferance
BEGIN
DROP TABLE IF EXISTS likeBuddy;
CREATE TABLE likeBuddy(
Buddy_name VARCHAR(150), Email VARCHAR(255), Phone CHAR(10));

	INSERT INTO likeBuddy ( Buddy_name, Email, Phone)
		SELECT au.first_name, au.email, au.Phone
        FROM auth_user au JOIN 
			(SELECT d.UserID, count(*)
			FROM Likes c JOIN Likes d ON c.UserID != d.UserID
			WHERE c.Score > 2 AND d.Score > 2 AND c.FeatureID = d.FeatureID AND c.UserID = UserId AND
            d.UserID IN (SELECT DISTINCT Schedule.UserID FROM Schedule WHERE Schedule.Date > subdate(curdate(), 180))
			GROUP BY d.UserID
			HAVING count(*) > 1) AS same ON au.id = same.UserID;
END;
BEGIN
SELECT * FROM matchBuddy;
SELECT * FROM matchRestaurant;
SELECT * FROM likeBuddy;
END;
END$$

DELIMITER ;
;
