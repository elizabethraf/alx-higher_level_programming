-- Import the database dump from hbtn_0d_tvshows to your MySQL server.
SELECT tv_genres.name FROM tv_genres WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = "Dexter") ORDER BY tv_genres.name;

