import sqlite3
import csv


def create_database(db_name="movies.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            movieCd TEXT PRIMARY KEY,
            movieNm TEXT,
            movieNmEn TEXT,
            prdtYear INTEGER,
            openDt TEXT,
            typeNm TEXT,
            prdtStatNm TEXT,
            nationAlt TEXT,
            genreAlt TEXT,
            repNationNm TEXT,
            repGenreNm TEXT
        )
    ''')

    conn.commit()
    conn.close()


def insert_data_from_csv(csv_file, db_name="movies.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row

        for row in reader:
            cursor.execute('''
                INSERT INTO movies (movieCd, movieNm, movieNmEn, prdtYear, openDt, typeNm, prdtStatNm, nationAlt, genreAlt, repNationNm, repGenreNm)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', row)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    csv_file = "kmdb_get_movie_list.csv"
    create_database()
    insert_data_from_csv(csv_file)
    print("Data inserted successfully!")
