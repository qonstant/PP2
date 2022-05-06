CREATE OR REPLACE PROCEDURE insert_many(list VARCHAR[][], SIZE INTEGER)
AS $$
BEGIN
FOR i IN 1..SIZE loop
INSERT INTO accounts
SELECT list[i][1], list[i][2] on conflict (username) DO UPDATE SET tell = list[i][2];
END loop;
END;
$$
LANGUAGE plpgsql;














