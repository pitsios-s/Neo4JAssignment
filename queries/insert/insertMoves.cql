CREATE INDEX ON :Move(id);

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS 
FROM 'file:/moves.csv' AS line 
CREATE (:Move {id: TOINT(line.id), number: TOINT(line.number), side: line.side, move: line.move, fen: line.fen});