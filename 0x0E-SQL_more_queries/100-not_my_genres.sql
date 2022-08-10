-- script that lists all genres that does not match with Dexter's
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
	-- sub query to find all genres that dexter matches with
	SELECT tv_genres.name
	FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
