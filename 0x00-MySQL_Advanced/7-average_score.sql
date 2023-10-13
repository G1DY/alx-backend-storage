-- a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INTEGER
)
BEGIN
	DECLARE total_score INTEGER;
	DECLARE total_corrections INTEGER;

	SELECT SUM(score) INTO total_score
	FROM corrections
	WHERE user_id = user_id;

	SELECT COUNT(*) INTO total_corrections
	FROM corrections
	WHERE user_id = user_id;

	IF total_corrections > 0 THEN
		UPDATE users
		SET average_score = total_score / total_corrections
		WHERE id = user_id;
	END IF;
END ; $$
DELIMITER ;
