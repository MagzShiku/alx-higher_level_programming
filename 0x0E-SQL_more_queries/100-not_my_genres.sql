--  script that uses the hbtn_0d_tvshows database to list all genres not
-- linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- sorted in ascending order by the genre name

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT sg.genre_id
	FROM tv_show_genres sg
	JOIN tv_shows s ON sg.show_id = s.id
	WHERE s.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
