CREATE INDEX ON :Game(id);

USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS 
FROM 'file:/games.csv' AS line
WITH line, SPLIT (line.date, '.') AS date
MATCH (e: Event {id: TOINT(line.eventID)}), (m: Move {id: TOINT(line.firstMoveID)})
MERGE (g: Game {id: TOINT(line.id), year: TOINT(date[0]), result: line.result, eco: line.eco, opening:line.opening, halfMoves: TOINT(line.halfMoves), moves: TOINT(line.moves), whiteELO: line.whiteELO, blackELO: line.blackELO})
CREATE (g)-[:belongsTo {round: TOINT(line.round)}]->(e)
CREATE (g)-[:startsWith]->(m);