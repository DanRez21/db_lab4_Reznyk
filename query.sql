-- 1.Вивести вина, які були вирощені в Іспанії
SELECT title 
FROM wine w
JOIN location_ l on w.wine_id = l.wine_id
WHERE l.country = 'Spain';

-- 2.Вивести ім'я та тег дегустатора, який поставив найвищий бал вину з США, як одне ім'я highest_rated_taster
SELECT CONCAT(TRIM(taster_name), ', ', TRIM(taster_twitter_handle)) AS highest_rated_taster
FROM taster
JOIN evaluation ON taster.taster_id = evaluation.taster_id
JOIN wine ON wine.eva_id = evaluation.eva_id
JOIN location_ ON wine.wine_id = location_.wine_id
WHERE location_.country = 'US'
ORDER BY evaluation.points DESC
LIMIT 1;

-- 3. Вивести провінцію наступного після найдорожчого вина.
SELECT province
FROM location_
JOIN wine ON wine.wine_id = location_.wine_id
ORDER BY wine.price DESC
LIMIT 1 OFFSET 1;