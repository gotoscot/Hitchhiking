CREATE DEFINER = CURRENT_USER TRIGGER `cs411`.`Schedule_AFTER_UPDATE` 
	AFTER UPDATE ON `Schedule` FOR EACH ROW
BEGIN
	SET @status = new.status;
    SET @date = new.date;
    SET @trailid = new.trailid;
    SET @userid = new.userid;
    
    IF @status = 'FALSE' THEN
		
		#Call find_budy();
	END IF;
END;

