CREATE OR REPLACE PROCEDURE insert_one(name VARCHAR(255), number VARCHAR(12))
AS $$
BEGIN
INSERT INTO accounts(username, tell) VALUES(name, number)
on conflict (username) DO UPDATE SET tell = number;
END; $$
LANGUAGE plpgsql;