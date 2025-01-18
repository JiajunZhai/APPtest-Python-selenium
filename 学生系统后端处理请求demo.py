from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨源请求

# 数据库连接参数
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'student-system'
}


def connect_to_database():
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None


def close_database_connection(connection):
    if connection:
        connection.close()


@app.route('/admin_login', methods=['GET'])
def admin_login():
    admin_name = request.args.get('admin_name')
    admin_pwd = request.args.get('admin_pwd')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM admin WHERE admin_name = %s AND admin_pwd = %s"
        cursor.execute(query, (admin_name, admin_pwd))
        results = cursor.fetchall()

        close_database_connection(connection)

        if results:
            return jsonify({'valid': True, 'message': '登录成功'})
        else:
            return jsonify({'valid': False, 'message': '用户名或密码错误'})
    else:
        return jsonify({'valid': False, 'message': '数据库连接错误'})


@app.route('/teacher_login', methods=['GET'])
def teacher_login():
    t_name = request.args.get('t_name')
    t_pwd = request.args.get('t_pwd')

    # 假设教师表名为 'teachers'
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM teachers WHERE t_name = %s AND t_pwd = %s"
        cursor.execute(query, (t_name, t_pwd))
        results = cursor.fetchall()

        close_database_connection(connection)

        if results:
            return jsonify({'valid': True, 'message': '教师登录成功'})
        else:
            return jsonify({'valid': False, 'message': '教师用户名或密码错误'})
    else:
        return jsonify({'valid': False, 'message': '数据库连接错误'})


@app.route('/student_login', methods=['GET'])
def student_login():
    s_no = request.args.get('s_no')
    s_pwd = request.args.get('s_pwd')

    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM students WHERE s_no = %s AND s_pwd = %s"
        cursor.execute(query, (s_no, s_pwd))
        results = cursor.fetchall()

        close_database_connection(connection)

        if results:
            return jsonify({'valid': True, 'message': '学生登录成功'})
        else:
            return jsonify({'valid': False, 'message': '学生用户名或密码错误'})
    else:
        return jsonify({'valid': False, 'message': '数据库连接错误'})


if __name__ == '__main__':
    app.run()
