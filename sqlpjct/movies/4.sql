SELECT COUNT (title) FROM movies
JOIN ratings ON ratings.movie_id = movies.id
WHERE ratings.rating LIKE "10.0";