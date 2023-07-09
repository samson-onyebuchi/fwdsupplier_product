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

class Brandsgateway(Resource):
    def post(self):
        try:
            # Mandated parameters
            mandated_params = ['product_type', 'group_sku', 'variation_type', 'product_sku', 'brand', 'name',
                               'retail_price', 'wholesale_price', 'main_picture', 'gender', 'category', 'subcategory',
                               'size', 'quantity', 'color', 'material', 'origin', 'product_id', 'weight', 'location',
                               'currency']

            # Check for mandated parameters
            missing_params = [param for param in mandated_params if param not in request.form]
            if missing_params:
                return {'message': f'Missing required fields: {", ".join(missing_params)}'}, 400

            # Construct product data
            product_data = {param: request.form[param] for param in mandated_params if param in request.form}

            # Optional parameters
            optional_params = ['description', 'product_code', 'size_slug', 'description_plain']

            # Add optional parameters if available
            for param in optional_params:
                if param in request.form:
                    product_data[param] = request.form[param]

            # Handle other_pictures parameter
            if 'other_pictures' in request.form:
                other_pictures = request.form.getlist('other_pictures')
                other_pictures_list = [{'picture': picture} for picture in other_pictures]
                product_data['other_pictures'] = other_pictures_list

            # Add default supplier_id parameter
            product_data['supplier_id'] = '001'

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

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

api.add_resource(Brandsgateway, '/product/Brandsgateway')
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

class Tradeeasy(Resource):
    def post(self):
        try:
            # Get all the parameters from the request
            category = request.form['category']
            gender = request.form['gender']
            photo = request.form['photo']
            article = request.form['article']
            model = request.form['model']
            size = request.form['size']
            quantity = int(request.form['quantity'])
            retail_price = float(request.form['retail_price'])
            wholesale_price = float(request.form['wholesale_price'])
            currency = request.form['currency']

            # Check if any of the parameters is missing or empty
            if not all([category, gender, photo, article, model, size, quantity, retail_price, wholesale_price, currency]):
                return {'message': 'Missing required fields'}, 400

            # Create a filter to check if the product already exists
            filter = {
                'category': category,
                'gender': gender,
                'article': article,
                'model': model,
                'size': size
            }

            # Create the product data
            product_data = {
                'category': category,
                'gender': gender,
                'photo': photo,
                'article': article,
                'model': model,
                'size': size,
                'quantity': quantity,
                'retail_price': retail_price,
                'wholesale_price': wholesale_price,
                'currency': currency,
                'supplier_id': '002'  # Add default supplier_id parameter
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

        except ValueError:
            return {'message': 'Invalid value provided for quantity, retail_price, or wholesale_price'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

api.add_resource(Tradeeasy, '/product/Tradeeasy')
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
                'rrp': rrp,
                'supplier_id': '003'  # Add default supplier_id parameter
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
api.add_resource(ADIDAS, '/product/ADIDAS')
""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

class DNC_WHOLESALE(Resource):
    def post(self):
        try:
            # List of mandatory parameters
            mandatory_params = ['store', 'lot', 'category', 'brand', 'description', 'color', 'size', 'quantity', 'retail_price', 'main_picture', 'currency']

            product_data = {}
            # Check and retrieve mandatory parameters from the request
            for param in mandatory_params:
                value = request.form.get(param)
                if not value:
                    return {'message': f'Missing mandatory parameter: {param}'}, 400
                product_data[param] = value

            # Check and retrieve optional parameter 'other_pictures' from the request
            other_pictures = request.form.getlist('other_pictures[]')
            if other_pictures:
                product_data['other_pictures'] = other_pictures

            # Check and retrieve optional parameter 'wholesale_quantity_price' from the request
            wholesale_quantity_price = request.form.getlist('wholesale_quantity_price[]')
            if wholesale_quantity_price:
                # Convert 'wholesale_quantity_price' to a list of dictionaries
                product_data['wholesale_quantity_price'] = [{'quantity': int(item.split(':')[0]), 'price': float(item.split(':')[1])} for item in wholesale_quantity_price]

            # Add default 'supplier_id' parameter
            product_data['supplier_id'] = '004'

            # Define the filter to check if the product already exists
            filter = {
                'store': product_data['store'],
                'lot_number': product_data['lot']
            }

            # Update or insert the product into the collection
            result = collection.update_one(filter, {'$set': product_data}, upsert=True)

            if result.upserted_id is not None:
                return {'message': 'Product inserted successfully'}
            elif result.modified_count > 0:
                return {'message': 'Product updated successfully'}
            else:
                return {'message': 'No changes made to the product'}

        except ValueError as e:
            return {'message': f'Invalid value for field: {e.args[0]}'}, 400

        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

# Resource routing
api.add_resource(DNC_WHOLESALE, '/product/DNC_WHOLESALE')



""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

class XMBO_offerCHARMEX(Resource):
    def post(self):
        try:
            main_picture = request.form.get('main_picture')
            other_pictures = request.form.getlist('other_pictures')
            brand = request.form.get('brand')
            ref = request.form.get('ref')
            article = request.form.get('article')
            ean = request.form.get('ean')
            description = request.form.get('description')
            hs = request.form.get('hs')
            material = request.form.get('material')
            made_in = request.form.get('made_in')
            quantity = request.form.get('quantity')
            retail_price = request.form.get('retail_price')
            wholesale_price = request.form.get('wholesale_price')
            currency = request.form.get('currency')

            # Validate mandatory parameters
            mandatory_params = [brand, article, ean, description, quantity, retail_price, wholesale_price, currency]
            if any(param is None for param in mandatory_params):
                return {'message': 'Mandatory parameters missing'}, 400

            quantity = int(quantity) if quantity else None
            retail_price = float(retail_price) if retail_price else None
            wholesale_price = float(wholesale_price) if wholesale_price else None

            product_data = {
                'main_picture': main_picture,
                'other_pictures': other_pictures,
                'brand': brand,
                'ref': ref,
                'article': article,
                'ean': ean,
                'description': description,
                'hs': hs,
                'material': material,
                'made_in': made_in,
                'quantity': quantity,
                'retail_price': retail_price,
                'wholesale_price': wholesale_price,
                'currency': currency,
                'supplier_id': '005'  # Add default supplier_id parameter
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

        except TypeError as te:
            return {'message': f'An error occurred: {str(te)}'}, 400
        except Exception as e:
            return {'message': f'An error occurred: {str(e)}'}, 500

api.add_resource(XMBO_offerCHARMEX, '/product/XMBO_offerCHARMEX')

"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
class AllDataResource(Resource):
    def get(self, supplier_id):
        try:
            # Retrieve documents from the collection based on supplier_id
            products = list(collection.find({'supplier_id': supplier_id}, {'_id': 0}))

            if products:
                response = {
                    'message': 'Products retrieved successfully.',
                    'data': products
                }
                return response
            else:
                return {'message': 'No products found for the specified supplier_id.'}, 404

        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500

api.add_resource(AllDataResource, '/ecommerce/products/<string:supplier_id>/record')


"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""

class DataResource(Resource):
    def get(self):
        try:
            # Retrieve all documents from the collection
            all_product = list(collection.find({}, {'_id': 0}))

            # Close the MongoDB connection
            client.close()

            if all_product:
                response = {
                    "message": "All products retrieved successfully.",
                    "data": all_product
                }
                return response
            else:
                return {'message': 'No data found in the collection.'}, 404

        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500


api.add_resource(DataResource, '/ecommerce/products/getall')