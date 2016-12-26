// QUERY 1
MATCH (g: Game)-[:startsWith]->(m1: Move)-[:leadsTo*]->(m2: Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH collect(g.result) AS results, count(g) AS NumOfGames
RETURN NumOfGames, ((size(filter(X in results where X = 'white')) / toFloat(NumOfGames))) * 100 AS WhiteWinPercentage;

// QUERY 2
MATCH (g: Game)-[:startsWith]->(m1: Move)-[:leadsTo*]->(m2: Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH collect(g.result) AS results, count(g) AS NumOfGames
RETURN NumOfGames, size(filter(X in results where X = 'white')) AS WhiteWins, 
    size(filter(X in results where X = 'black')) AS BlackWins, 
    size(filter(X in results where X = 'draw')) AS Draws;

// QUERY 3
MATCH (g1: Game)-[:belongsTo]->(e1: Event)
WITH e1, count(g1.id) as total
WITH max(total) as m
MATCH (p2: Player)-[:playsIn]->(g2: Game)-[:belongsTo]->(e2: Event)
WITH e2, count(distinct(g2)) as TotalGames, m, collect(p2.name) as names
WHERE TotalGames = m
RETURN e2.name AS EventName, 
    TotalGames, 
    size(filter(X in names where X = "Karpov  Anatoly")) AS KarpovAnatolyGames;

// QUERY 4
MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(distinct(g)) AS numOfGames
WITH collect({playerName: playerName, numOfGames: numOfGames}) AS collection, max(numOfGames) AS maximum
UNWIND filter(X in collection WHERE X.numOfGames = maximum) as rows
RETURN rows;

MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(distinct(g)) AS numOfGames
WITH max(numOfGames) as maxGames
MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(distinct(g)) AS numOfGames, maxGames
WHERE numOfGames = maxGames
RETURN playerName, numOfGames;

MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(distinct(g)) AS numOfGames
ORDER BY numOfGames DESC
RETURN playerName, numOfGames;