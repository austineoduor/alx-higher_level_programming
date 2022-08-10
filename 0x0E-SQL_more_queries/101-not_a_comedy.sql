-- list all shows that are not a comedy
SELECT tv_shows.title 'title'
FROM tv_shows
WHERE tv_shows.title NOT IN (
	-- subquery that selects all shows that are comedies
	SELECT tv_shows.title
	FROM tv_shows
	INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id 
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY title
