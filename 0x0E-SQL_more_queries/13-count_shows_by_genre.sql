-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- select the two columns and join where the ids match. only show nulls
SELECT tv_genres.name 'genre', COUNT(*) 'number_of_shows'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC
