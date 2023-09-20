-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy
-- Each record should display: tv_shows.title
-- sorted in ascending order by the show title

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT sg.show_id
	FROM tv_show_genres sg
	JOIN tv_genres g ON sg.genre_id = g.id
	WHERE g.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
