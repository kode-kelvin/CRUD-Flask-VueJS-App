from flask import  Flask, jsonify, request
from flask_sqlalchemy import  SQLAlchemy
import datetime
from flask_marshmallow import  Marshmallow
from flask_cors import  CORS



# settings
app = Flask(__name__)
CORS(app)



app.config['SQLALCHEMY_DATABASE_URI']  =  'sqlite:///articledatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db = SQLAlchemy(app)
ma = Marshmallow(app)



# table
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body= db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body

# schema
class ArticleSchema(ma.Schema):
    class  Meta:
        fields = ("id", "title", "body", "date")


# schema obj
article_schema = ArticleSchema() 
articles_schema = ArticleSchema(many=True) 

# routes

#  ------------------ get all
@app.route('/ape_blog/api/v1.0/articles', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    return  articles_schema.jsonify(all_articles)


#  ------------------ get by ID
@app.route('/ape_blog/api/v1.0/article/<id>/', methods=['GET'])
def article_details(id):

    article_detail = Articles.query.get(id)
    if article_detail:
        return article_schema.jsonify(article_detail)
    else:
        return "No article with that ID"
    


#  ------------------ post or add new 
@app.route('/ape_blog/api/v1.0/article', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

#  ------------------ update individual
@app.route('/ape_blog/api/v1.0/article/<id>/', methods=['PUT'])
def update_article(id):
    update_article = Articles.query.get(id)
    update_article.title = request.json['title']
    update_article.body = request.json['body']
    db.session.commit()
    return article_schema.jsonify(update_article)


#  ------------------ delete individual
@app.route('/ape_blog/api/v1.0/article/<id>/', methods=['DELETE'])
def delete_article(id):
    delete_article = Articles.query.get(id)
    db.session.delete(delete_article)
    db.session.commit()
    return article_schema.jsonify(delete_article)


    


if __name__ == '__main__':
    app.run(debug=True)
