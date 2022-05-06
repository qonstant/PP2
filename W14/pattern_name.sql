CREATE OR REPLACE FUNCTION pattern_names(p_pattern VARCHAR)
    RETURNS TABLE (
        account_username VARCHAR,
        account_tell VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT
        username,
        tell
    FROM
        accounts
    WHERE
        username LIKE p_pattern;
END; $$
LANGUAGE plpgsql;