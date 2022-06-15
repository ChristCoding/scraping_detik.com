import psycopg2
from postgre_dbase.config import config


def insert_vendor(product_name,product_link,product_img_link,product_price):
    sql =("""INSERT INTO carousell(product_name,product_link,product_img_link,product_price) VALUES(%s,%s,%s,%s) RETURNING product_id;""")

    conn=None
    product_id=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute(sql,(product_name,product_link,product_img_link,product_price,))
        vendor_id=cur.fetchone()[0]
        print(vendor_id)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
