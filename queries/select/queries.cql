// QUERY 1
MATCH (g: Game)-[:startWith]->(m1: Move)-[:leadsTo*]->(m2: Move {fen: 'r1bqkbnrpppp1ppp2n51B2p34P35N2PPPP1PPPRNBQK2R'})
WITH g
RETURN COUNT(g) AS NumOfGames;