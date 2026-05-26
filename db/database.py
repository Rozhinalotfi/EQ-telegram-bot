import sqlite3
import datetime

DB_FILE = "database.db"
MAX_TOTAL = 100

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id                   INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id          INTEGER,
            username             TEXT,
            gender               TEXT,
            age                  INTEGER,

            -- نمره کل
            total_score          INTEGER,
            total_max            INTEGER,
            total_pct            REAL,

            -- ۵ مقیاس کلی (درصد)
            comp_intrapersonal   REAL,
            comp_interpersonal   REAL,
            comp_adaptability    REAL,
            comp_stress          REAL,
            comp_mood            REAL,

            -- ۱۵ زیرمقیاس (نمره خام)
            sub_1  INTEGER, sub_2  INTEGER, sub_3  INTEGER,
            sub_4  INTEGER, sub_5  INTEGER, sub_6  INTEGER,
            sub_7  INTEGER, sub_8  INTEGER, sub_9  INTEGER,
            sub_10 INTEGER, sub_11 INTEGER, sub_12 INTEGER,
            sub_13 INTEGER, sub_14 INTEGER, sub_15 INTEGER,

            -- ۱۵ زیرمقیاس (درصد)
            sub_pct_1  REAL, sub_pct_2  REAL, sub_pct_3  REAL,
            sub_pct_4  REAL, sub_pct_5  REAL, sub_pct_6  REAL,
            sub_pct_7  REAL, sub_pct_8  REAL, sub_pct_9  REAL,
            sub_pct_10 REAL, sub_pct_11 REAL, sub_pct_12 REAL,
            sub_pct_13 REAL, sub_pct_14 REAL, sub_pct_15 REAL,

            created_at           TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_result(
    telegram_id, username, gender, age,
    total_score, total_pct,
    comp_pcts,
    sub_scores,
    sub_pcts
):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("""
        INSERT INTO results (
            telegram_id, username, gender, age,
            total_score, total_max, total_pct,
            comp_intrapersonal, comp_interpersonal, comp_adaptability,
            comp_stress, comp_mood,
            sub_1, sub_2, sub_3, sub_4, sub_5,
            sub_6, sub_7, sub_8, sub_9, sub_10,
            sub_11, sub_12, sub_13, sub_14, sub_15,
            sub_pct_1, sub_pct_2, sub_pct_3, sub_pct_4, sub_pct_5,
            sub_pct_6, sub_pct_7, sub_pct_8, sub_pct_9, sub_pct_10,
            sub_pct_11, sub_pct_12, sub_pct_13, sub_pct_14, sub_pct_15,
            created_at
        ) VALUES (
            ?, ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,
            ?
        )
    """, (
        telegram_id, username, gender, age,
        total_score, MAX_TOTAL, round(total_pct, 2),
        *comp_pcts,
        *sub_scores,
        *[round(p, 2) for p in sub_pcts],
        datetime.datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()