CREATE INDEX ON :Player(id);
CREATE CONSTRAINT ON (p:Player) ASSERT p.name IS UNIQUE;

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS 
FROM 'file:/players.csv' AS line 
CREATE (:Player {id: TOINT(line.id), name: line.name});