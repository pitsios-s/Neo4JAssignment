CREATE INDEX ON :Event(id);
CREATE CONSTRAINT ON (e: Event) ASSERT e.name IS UNIQUE;

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS 
FROM 'file:/events.csv' AS line
WITH line, SPLIT (line.date, '.') AS date
MERGE (:Event {id: TOINT(line.id), name: line.name, site: line.site, year: TOINT(date[0])});