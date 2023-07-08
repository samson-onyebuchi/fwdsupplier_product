from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
from pymongo import MongoClient
import os

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))
db = client["TENCOWRY"]
collection = db["TenCowry_eCommerce"]



app = Flask(__name__)
api = Api(app)

class BrandsgatewayCSV_Example_2(Resource):
    def post(self):
        try:
            product_data = {
                'product_type': request.form['product_type'],
                'group_sku': request.form['group_sku'],
                'variation_type': request.form['variation_type'],
                'product_sku': request.form['product_sku'],
                'brand': request.form['brand'],
                'name': request.form['name'],
                'retail_price': float(request.form['retail_price']),
                'wholesale_price': float(request.form['wholesale_price']),
                'description': request.form['description'],
                'main_picture': request.form['main_picture'],  # Store as link directly
                'gender': request.form['gender'],
                'category': request.form['category'],
                'subcategory': request.form['subcategory'],
                'size': request.form['size'],
                'quantity': int(request.form['quantity']),
                'color': request.form['color'],
                'material': request.form['material'],
                'product_code': request.form['product_code'],
                'origin': request.form['origin'],
                'product_id': request.form['product_id'],
                'size_slug': request.form['size_slug'],
                'description_plain': request.form['description_plain'],
                'weight': float(request.form['weight']),
                'location': request.form['location'],
                'currency': request.form['currency'],
                'other_pictures': [{ 'picture': 'link1' }, { 'picture': 'link2' }]
            }

            # Define the filter to check if the product already exists
            filter = {
                'Product Id': product_data['Product Id']
            }

            # Update or insert the product into the collection
            result = collection.update_one(filter, {'$set': product_data}, upsert=True)

            if result.upserted_id is not None:
                return {'message': 'Product inserted successfully'}
            else:
                if result.modified_count > 0:
                    return {'message': 'Product updated successfully'}
                else:
                    return {'message': 'No changes made to the product'}

        except KeyError as e:
            return {'message': f'Missing required field: {e.args[0]}'}, 400

        except ValueError as e:
            return {'message': f'Invalid value for field: {e.args[0]}'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

api.add_resource(BrandsgatewayCSV_Example_2, "/product/BrandsgatewayCSV_Example_2")

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

class Example_Lot(Resource):    
    def post(self):
        try:
            brand_name = request.form.get('brand_name')
            item_description = request.form.get('item_description')
            color = request.form.get('color')
            size = request.form.get('size')
            original_qty = request.form.get('original_qty')
            original_retail_price = request.form.get('original_retail_price')
            image = request.form.get('image')

            # Create a filter to check if the product already exists
            filter = {
                'brand_name': brand_name,
                'item_description': item_description,
                'color': color,
                'size': size
            }

            # Create the product data
            product_data = {
                'brand_name': brand_name,
                'item_description': item_description,
                'color': color,
                'size': size,
                'original_qty': original_qty,
                'original_retail_price': original_retail_price,
                'image': image
            }

            # Update or insert the product into the collection
            result = collection.update_one(filter, {'$set': product_data}, upsert=True)

            if result.upserted_id is not None:
                return {'message': 'Product inserted successfully'}
            else:
                if result.modified_count > 0:
                    return {'message': 'Product updated successfully'}
                else:
                    return {'message': 'No changes made to the product'}

        except KeyError as e:
            return {'message': f'Missing required field: {e.args[0]}'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

api.add_resource(Example_Lot, "/product/Example_Lot")

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""


class ADIDAS(Resource):
    def post(self):
        try:
            photo = request.form.get('photo')
            article = request.form.get('article')
            model = request.form.get('model')
            size = request.form.get('size')
            total = request.form.get('total')
            price = request.form.get('price')
            rrp = request.form.get('rrp')

            # Create a filter to check if the product already exists
            filter = {
                'article': article
            }

            # Create the product data
            product_data = {
                'photo': photo,
                'article': article,
                'model': model,
                'sizes': size,
                'total': total,
                'price': price,
                'rrp': rrp
            }

            # Update or insert the product into the collection
            result = collection.update_one(filter, {'$set': product_data}, upsert=True)

            if result.upserted_id is not None:
                return {'message': 'Product inserted successfully'}
            else:
                if result.modified_count > 0:
                    return {'message': 'Product updated successfully'}
                else:
                    return {'message': 'No changes made to the product'}

        except KeyError as e:
            return {'message': f'Missing required field: {e.args[0]}'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500


api.add_resource(ADIDAS, "/product/ADIDAS_IN_STOCK")


""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

class DNC_WHOLESALE(Resource):    
    def post(self):
        try:
            store = request.form.get('store')
            lot_number = request.form.get('lot_number')
            category = request.form.get('merchandise_category')
            quantity = request.form.get('quantity')
            unit_price = request.form.get('unit_price')

            product_data = {
                'store': store,
                'lot_number': lot_number,
                'merchandise_category': category,
                'quantity': quantity,
                'unit_price': unit_price
            }

            # Define the filter to check if the product already exists
            filter = {
                'store': store,
                'lot_number': lot_number
            }

            # Update or insert the product into the collection
            result = collection.update_one(filter, {'$set': product_data}, upsert=True)

            if result.upserted_id is not None:
                return {'message': 'Product inserted successfully'}
            else:
                if result.modified_count > 0:
                    return {'message': 'Product updated successfully'}
                else:
                    return {'message': 'No changes made to the product'}

        except ValueError as e:
            return {'message': f'Invalid value for field: {e.args[0]}'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500


api.add_resource(DNC_WHOLESALE, '/product/DNC_WHOLESALE_DISTRIBUTOR_PRICE_LIST_collection')

""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

class XMBO_offerCHARMEX(Resource):    
    def post(self):
        try:
            picture = request.form.get('picture')
            ref = request.form.get('ref')
            brand = request.form.get('brand')
            description = request.form.get('description')
            hs = request.form.get('hs')
            material = request.form.get('material')
            made_in = request.form.get('made_in')
            qty = request.form.get('qty')
            retail_price = request.form.get('retail_price')

            product_data = {
                'picture': picture,
                'ref': ref,
                'brand': brand,
                'description': description,
                'hs': hs,
                'material': material,
                'made_in': made_in,
                'qty': qty,
                'retail_price': retail_price
            }

            # Define the filter to check if the product already exists
            filter = {
                'ref': ref
            }

            # Update or insert the product into the collection
            result = collection.update_one(filter, {'$set': product_data}, upsert=True)

            if result.upserted_id is not None:
                return {'message': 'Product inserted successfully'}
            else:
                if result.modified_count > 0:
                    return {'message': 'Product updated successfully'}
                else:
                    return {'message': 'No changes made to the product'}

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

api.add_resource(XMBO_offerCHARMEX, '/product/XMBO_offerCHARMEX')



