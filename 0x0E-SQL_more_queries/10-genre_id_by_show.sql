-- script that lists all shows in 'hbtn_0d_tvshows' with atleast one genre
-- Each record displays
-- tv_shows.title, tv_show_genres.genre_id
-- The results are in ascending order bt tv_shows.title and tv_shows_genre
-- .genre_id using SELECT once
SELECT tv_shows.title, tv_show_genres.genres_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre.id;
