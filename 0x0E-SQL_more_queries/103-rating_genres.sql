-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- Each record should display: tv_genres.name - rating sum
-- sorted in descending order by their rating

SELECT g.name, SUM(r.rate) AS rating_sum
FROM tv_genres AS g
LEFT JOIN (
	SELECT sg.genre_id, sr.rate
	FROM tv_show_genres AS sg
	LEFT JOIN tv_show_ratings AS sr ON sg.show_id = sr.show_id
) AS r ON g.id = r.genre_id
GROUP BY g.name
ORDER BY rating_sum DESC;
