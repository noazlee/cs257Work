DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime text,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text,
  id text,
  updated text,
  place text,
  status2 text,
  locationSource text
);