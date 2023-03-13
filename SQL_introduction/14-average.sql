-- computes the score average of all records in the table second_table
ALTER TABLE second_table ADD COLUMN average INT;

INSERT INTO second_table (average)
VALUES (AVG(SCORE));
