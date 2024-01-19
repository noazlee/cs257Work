-- Fetch all the data from eathuqakes with a magnitude higher than 6 sorted from highest to lowest
SELECT * FROM earthquakes WHERE mag>6 ORDER BY mag DESC;
-- Fetch all the data from earthquakes in a longitude between -180 and -130 and a latitude between 52 and 71
SELECT * FROM earthquakes WHERE longitude BETWEEN -180 AND -130 AND latitude BETWEEN 52 AND 71;
-- quaketime is in datatype text and not date so cannot do that query.

-- fetch the place and magnitude of the earthquake where the magnitude is larger than 6 and between latitudes 50 and 70 ordered from lowest magnitude to highest.
SELECT place, mag WHERE mag > 6 AND latitude BETWEEN 50 AND 70 ORDER BY mag ASC;