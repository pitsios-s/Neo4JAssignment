USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS 
FROM 'file:/moveMove.csv' AS line
MATCH (m1: Move {id: TOINT(line.moveId)}), (m2: Move {id: TOINT(line.nextMoveId)})
CREATE (m1)-[:leadsTo]->(m2);