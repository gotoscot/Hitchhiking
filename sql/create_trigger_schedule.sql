DROP TRIGGER IF EXISTS `cs411`.`Schedule_BEFORE_UPDATE`;

DELIMITER $$
USE `cs411`$$
CREATE DEFINER = CURRENT_USER TRIGGER `cs411`.`Schedule_BEFORE_UPDATE` 
	BEFORE UPDATE ON `Schedule` FOR EACH ROW
BEGIN
	SET @status = new.status;
    SET @date = new.date;
    SET @msg = '';
    
    IF @status = 'TRUE'  AND @date > CURDATE() THEN
		SET @msg = concat('The hiking date: ', cast(new.date as char), ' is in the future');
        signal sqlstate '45000' set message_text = @msg;

	END IF;
    IF @status = 'FALSE' THEN
		SET new.rating = 0;
	END IF;
END;$$
DELIMITER ;