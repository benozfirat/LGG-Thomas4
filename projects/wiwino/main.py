import sqlite3

def main():
  return False

if __name__ == "__main__":
    main()

connexion = sqlite3.connect("db/vivino.db")
cursor = connexion.cursor()

#We want to highlight 10 wines to increase our sales. Which ones should we choose and why?


query1 = f"""
    SELECT
      name,
      ratings_average
    FROM
      wines
    WHERE 
      ratingS_count > 10000 
    ORDER BY
      ratings_average DESC
    LIMIT 10;
"""

cursor.execute(query1)
for row in cursor.fetchall():
   print(row)

#We have a limited marketing budget for this year. Which country should we prioritise and why?


query2 = f"""
    SELECT
      name,
      users_count
    FROM
      countries 
    ORDER BY
      users_count DESC
    LIMIT 1;
"""
cursor.execute(query2)
country = cursor.fetchall()[0]

print(country)

#We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?
#Best rated 
query3 = f"""
    SELECT
      wineries.name
    FROM
      wineries
      JOIN wines on wineries.Id = wines.winery_id   
    ORDER BY
      ratings_average DESC
    LIMIT 1;
"""
cursor.execute(query3)
best_ratings = cursor.fetchall()[0]
print(best_ratings)

#Best Vintage
query4 = f"""
    SELECT
      wineries.name
    FROM
      wineries
      JOIN wines ON wineries.Id = wines.winery_id   
      JOIN vintages ON vintages.wine_id = wines.id
    ORDER BY
      vintages.ratings_average DESC
    LIMIT 1;
"""

cursor.execute(query4)
best_vintage_ratings = cursor.fetchall()[0]
print(best_ratings)

#Sweetest wine
query5 = f"""
    SELECT
      wineries.name
    FROM
      wineries
      JOIN wines on wineries.Id = wines.winery_id   
    ORDER BY
      sweetness DESC
    LIMIT 1;
"""
cursor.execute(query5)
best_ratings = cursor.fetchall()[0]
print(best_ratings)
