USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS 
FROM 'file:/playersGames.csv' AS line
MATCH (p: Player {id: TOINT(line.playerID)}), (g: Game {id: TOINT(line.gameID)})
CREATE (p)-[:playsIn {color: line.color}]->(g);