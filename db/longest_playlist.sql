SELECT
	p.PlaylistId,
	p.Name,
	count(1) AS TracksCount,
	sum(t.Milliseconds) / 1000 / 60 AS Minutes
FROM tracks AS t
JOIN playlist_track AS pt ON t.TrackId = pt.TrackId
JOIN playlists AS p ON pt.PlaylistId = p.PlaylistId
GROUP BY p.PlaylistId
ORDER BY Minutes DESC
LIMIT 1;
