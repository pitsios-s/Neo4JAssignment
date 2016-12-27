// QUERY 1
// Approach 1
MATCH (g: Game)-[*]->(:Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH collect(g.result) AS results, count(g) AS NumOfGames
RETURN NumOfGames, ((size(filter(X in results where X = 'white')) / toFloat(NumOfGames))) * 100 AS WhiteWinPercentage;

// Approach 2
MATCH (g: Game)-[:startsWith]->(m1: Move)-[:leadsTo*]->(m2: Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH collect(g.result) AS results, count(g) AS NumOfGames
RETURN NumOfGames, ((size(filter(X in results where X = 'white')) / toFloat(NumOfGames))) * 100 AS WhiteWinPercentage;

// QUERY 2
// Approach 1
MATCH (g: Game)-[*]->(:Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH collect(g.result) AS results, count(g) AS NumOfGames
RETURN NumOfGames, size(filter(X in results where X = 'white')) AS WhiteWins, 
    size(filter(X in results where X = 'black')) AS BlackWins, 
    size(filter(X in results where X = 'draw')) AS Draws;

// Approach 2
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
WITH e2, count(DISTINCT g2) as TotalGames, m, collect(p2.name) as names
WHERE TotalGames = m
RETURN e2.name AS EventName, 
    TotalGames, 
    size(filter(X in names where X = "Karpov  Anatoly")) AS KarpovAnatolyGames;

// QUERY 4
// Approach 1
MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(DISTINCT g) AS numOfGames
WITH collect({playerName: playerName, numOfGames: numOfGames}) AS collection, max(numOfGames) AS maximum
UNWIND filter(X in collection WHERE X.numOfGames = maximum) as rows
RETURN rows;

// Approach 2
MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(DISTINCT g) AS numOfGames
WITH max(numOfGames) as maxGames
MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(DISTINCT g) AS numOfGames, maxGames
WHERE numOfGames = maxGames
RETURN playerName, numOfGames;

// Approach 3
MATCH (p: Player)-[:playsIn]->(g: Game {opening: 'Ruy Lopez'})
WITH p.name AS playerName, count(DISTINCT g) AS numOfGames
ORDER BY numOfGames DESC
RETURN playerName, numOfGames;

// QUERY 5
MATCH (p: Player)-[:playsIn]->(g: Game)-
	[:startsWith]->(m: Move)-
    [:leadsTo*]->(m1: Move {move: 'Nc6'})-
    [:leadsTo]->(m2: Move {move: 'Bb5'})-
    [:leadsTo]->(m3: Move {move: 'a6'})
WITH count(DISTINCT g) AS NumOfGames, collect(DISTINCT p.name) AS PlayerNames
RETURN NumOfGames, PlayerNames;

// QUERY 6
MATCH (p: Player)-[pin: playsIn]->(g: Game {id: 363})-[*]->(m: Move)
WITH g, collect(DISTINCT {PlayerName: p.name, Color: pin.color}) AS players, 
    collect(DISTINCT {number: m.id, move: m.move}) AS allMoves
RETURN g.id AS GameNumber,
	players AS Players,
	g.year AS GameYear, 
	g.result AS Result,
    g.halfMoves AS HalfMoves,
    g.moves AS Moves,
    g.whiteELO AS WhiteELO,
    g.blackELO AS BlackELO,
    g.eco AS ECO,
    g.opening AS Opening,
    allMoves;

// QUERY 7