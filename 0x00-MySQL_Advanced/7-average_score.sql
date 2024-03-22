-- Create stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student

-- DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Calculate total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate total number of projects for the user
    SELECT COUNT(DISTINCT project_id) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Compute average score and update users table
    IF total_projects > 0 THEN
        UPDATE users
        SET average_score = total_score / total_projects
        WHERE id = user_id;
    END IF;
END;
//
DELIMITER ;