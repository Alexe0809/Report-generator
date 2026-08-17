from database import connect


def get_total_revenue():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT SUM(quantity * price) FROM orders WHERE status='completed';"""
    )
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result


def get_order_count():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT COUNT(*) FROM orders;"""
    )
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result


def get_average_check():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT AVG(quantity * price) FROM orders WHERE status='completed';"""
    )
    result = cur.fetchone()[0]
    cur.close()
    conn.close()
    return result


def get_sales_by_product():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT product, SUM(quantity * price) FROM orders WHERE status='completed' GROUP BY product ORDER BY SUM(quantity * price) DESC;"""
    )
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def get_sales_by_customer():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT customer, SUM(quantity * price) FROM orders WHERE status='completed' GROUP BY customer ORDER BY SUM(quantity * price) DESC;"""
    )
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def get_sales_by_day():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        """SELECT date, SUM(quantity * price) FROM orders WHERE status='completed' GROUP BY date ORDER BY date;"""
    )
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


if __name__ == "__main__":
    print("Revenue:", get_total_revenue())
    print("Orders:", get_order_count())
    print("Average check:", get_average_check())
    print("By product:", get_sales_by_product())
    print("By customer:", get_sales_by_customer())
    print("By date:", get_sales_by_day())