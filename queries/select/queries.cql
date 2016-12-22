// QUERY 1
MATCH (g: Game)-[:startWith]->(m1: Move)-[:leadsTo*]->(m2: Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH collect(g.result) AS results, count(g) AS NumOfGames
RETURN NumOfGames, ((size(filter(X in results where X = 'white')) / toFloat(size(results)))) * 100 AS WhiteWinPercentage;