from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# 数据库连接配置
DB_HOST = '119.3.125.38'
DB_USER = 'root'
DB_PASSWORD = 'qQ123456'
DB_DATABASE = 'sql1'

# 创建数据库连接
db = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
cursor = db.cursor()

# POST请求处理函数
@app.route('/api/post', methods=['POST'])
def post_data():
    # 从POST请求中获取JSON数据
    data = request.json
    
    # 获取版本号
    version = data.get('version')

    # 插入数据到数据库表中
    try:
        sql = "INSERT INTO 启动器(version) VALUES (%s)"
        cursor.execute(sql, (version,))
        db.commit()
        message = "Data posted successfully"
    except Exception as e:
        db.rollback()
        message = f"Error: {str(e)}"
    
    # 返回消息
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=443)
