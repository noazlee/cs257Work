DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text(255),
  id text(255),
  updated text(255),
  place text,
  status text,
  locationSource text
);