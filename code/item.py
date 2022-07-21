import sqlite3
from flask import request
# from unittest import result
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required


class Item(Resource):
    # @jwt_required()
    def get(self,name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'messages' : 'Item not found'}

          # item = next(filter(lambda x : x['name'] == name , items), None)
        # for item in items:
        #     if item['name'] == name :
        #         return {'item' : item}
        #     else:
        #         None 

       

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=:name"
        result = cursor.execute(query,{"name":name})

        row = result.fetchone()
        connection.close()

        if row:
            return {'item' : {'name' : row[0],'price' : row[1]}}
        

    def post(self,name):
        if self.find_by_name(name):
            return {'message' : "An item with name '{}' already exists" .format(name)}

        data = request.get_json()
        item = {
            'name' : name,
            'price': data['price']
        }
        try:
            self.insert(item)
        except:
            return {'message' : 'An error occurerd inserting the item'}

        return item


    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(query,(item['name'],item['price']))
        
        connection.commit()
        connection.close()

        # if next(filter(lambda x : x['name'] == name,items) , None):
        #     return {'message' : "An item with name '{}' aleady exis " . format(name)}
        
        # for x in items :
        #     if x['name'] == name:
        #         return {'message' : "An item with name '{}' aleady exis" .format(name)}
        #     else :
        #         data = request.get_json()
        #         item = {
        #             'name' : name , 
        #             'price' : data['price']
        #         }
        #         items.append(item)
        #         return item

    # @jwt_required
    def delete(self,name):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=:name"
        cursor.execute(query,{"name":name})

        connection.commit()
        connection.close()
        
        return {'message' : ' Item deleted'}



            
        # global item
        # items = list(filter(lambda x : x['name'] != name , items) )
        # return {'message' : ' Item deleted'}

    # @jwt_required
    def put(self,name):
        # parser = reqparse.RequestParser()
        # parser.add_argument('price',type = float , required = True , help = "the price is not null")
        # data = parser.parse_args()
        data = request.get_json() #nhap du lieu
        item = self.find_by_name(name)
        update_item = {
            'name' : name,
            'price' : data['price']
        }
        if item is None :
            try:
                self.insert(update_item)
            except:
                return {"message" : "insert errors"}
        else :
            try:
                self.update(update_item)
            except:
                return {"message" : "update errors"}
        return item

    @classmethod
    def update(cls,item):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(item['name'],item['price']))
        
        connection.commit()
        connection.close()
            

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.sqlite')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)

        row = result.fetchall()
        connection.close()

        if row:
            return {'items' : {'item' : {'name' : row[0],'price' : row[1]}}}
        return {'messages' : 'Item not found'}


