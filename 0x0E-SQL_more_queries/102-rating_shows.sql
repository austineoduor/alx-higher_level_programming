-- shows the top rating shows
SELECT tv_shows.title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
-- join the ratings by id and show id
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER by rating DESC
