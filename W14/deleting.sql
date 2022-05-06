CREATE OR REPLACE PROCEDURE deleting(name VARCHAR(255))
AS $$
BEGIN
DELETE FROM accounts WHERE username = name
ON conflict (username)
END; $$
LANGUAGE plpgsql;