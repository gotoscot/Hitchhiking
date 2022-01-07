CREATE DEFINER = CURRENT_USER TRIGGER `cs411`.`INSERT_UPDATE` BEFORE INSERT ON `Likes` FOR EACH ROW
BEGIN
	IF (SELECT LikeID FROM Likes WHERE UserID = new.UserID AND FeatureID = new.FeatureID) THEN
		UPDATE Likes SET Score = new.Score WHERE UserID = new.UserID AND FeatureID = new.FeatureID;
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'The feature score is updated!';
	ELSE
		SIGNAL SQLSTATE '01000' SET MESSAGE_TEXT = 'The feature is added!';
	END IF;
END
