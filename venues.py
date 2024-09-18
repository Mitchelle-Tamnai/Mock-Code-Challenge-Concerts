from db_connection import get_connection

class Venues:
    def __init__(self, id):
        self.id = id
    
    def bands(self):
        conn = get_connection()
        if conn is not None:
            cur = conn.cursor()
            cur.execute(('''
                SELECT band.name, 
                         band.hometown 
                FROM concert
                INNER JOIN band ON concert.band_id = band.id
                         INNER JOIN venue ON venue.id = concert.venue_id
                WHERE venue.id= %s
            '''), (self.id,))
            bands = cur.fetchall()
            cur.close()
            conn.close()
            return bands
        else:
            return []
    def concerts(self):
             conn = get_connection()
             if conn is not None:
                 cur = conn.cursor()
                 cur.execute(('''
                     SELECT concert.concert_name, 
                              concert.date,
                              band.name 
                     FROM concert
                     INNER JOIN band ON concert.band_id = band.id
                              INNER JOIN venue ON venue.id = concert.venue_id
                     WHERE venue.id= %s
                 '''), (self.id,))
                 concerts = cur.fetchall()
                 cur.close()
                 conn.close()
                 return concerts
             else:
                 return []
        
    def concert_on(self, date):
         conn = get_connection()
         if conn is not None:
             cur = conn.cursor()
             cur.execute(('''
                 SELECT concert.concert_name, 
                          concert.date,
                          band.name 
                 FROM concert
                 INNER JOIN band ON concert.band_id = band.id
                          INNER JOIN venue ON venue.id = concert.venue_id
                 WHERE venue.id= %s AND concert.date = %s
             '''), (self.id, date))
             concert = cur.fetchone()
             cur.close()
             conn.close()
             return concert[0] if concert else None
         else:
             return None

    def most_frequent_band(self):
         conn = get_connection()
         if conn is not None:
             cur = conn.cursor()
             cur.execute(('''
                 SELECT band.name, 
                          COUNT(*) as total
                 FROM concert
                 INNER JOIN band ON concert.band_id = band.id
                          INNER JOIN venue ON venue.id = concert.venue_id
                 WHERE venue.id= %s
                 GROUP BY band.name
                 ORDER BY total DESC
                 LIMIT 1
             '''), (self.id,))
             most_frequent_band = cur.fetchone()
             cur.close()
             conn.close()
             return most_frequent_band[0] if most_frequent_band else None
         else:
             return None
         



