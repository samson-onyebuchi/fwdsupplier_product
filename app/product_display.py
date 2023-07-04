from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import os

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))
db = client["fwdsupplierproductfile"]
collection = db["BrandsgatewayCSV Example 2"]


app = Flask(__name__)
api = Api(app)

class BrandsgatewayCSV_Example_2(Resource):
    def post(self):
        try:
            product_data = {
                'Product Type': request.form['Product Type'],
                'Group Sku': request.form['Group Sku'],
                'Variation Type': request.form['Variation Type'],
                'Product Sku': request.form['Product Sku'],
                'Brand': request.form['Brand'],
                'Name': request.form['Name'],
                'Retail Price': float(request.form['Retail Price']),
                'Wholesale Price': float(request.form['Wholesale Price']),
                'Description': request.form['Description'],
                'Main Picture': request.form['Main Picture'],  # Store as link directly
                'Gender': request.form['Gender'],
                'Category': request.form['Category'],
                'Subcategory': request.form['Subcategory'],
                'Size': request.form['Size'],
                'Quantity': int(request.form['Quantity']),
                'Color': request.form['Color'],
                'Material': request.form['Material'],
                'Product Code': request.form['Product Code'],
                'Origin': request.form['Origin'],
                'Product Id': request.form['Product Id'],
                'Size Slug': request.form['Size Slug'],
                'Description Plain': request.form['Description Plain'],
                'Weight': float(request.form['Weight']),
                'Location': request.form['Location'],
                'Currency': request.form['Currency']
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

collection_example_lot = db["Example Lot"]

class Example_Lot(Resource):
    def post(self):
        try:
            brand_name = request.form.get('BRAND NAME')
            item_description = request.form.get('ITEM DESCRIPTION')
            color = request.form.get('COLOR')
            size = request.form.get('SIZE')
            original_qty = request.form.get('ORIGINAL QTY')
            original_retail_price = request.form.get('ORIGINAL RETAIL PRICE')
            image = request.form.get('IMAGE')

            # Create a filter to check if the product already exists
            filter = {
                'BRAND NAME': brand_name,
                'ITEM DESCRIPTION': item_description,
                'COLOR': color,
                'SIZE': size
            }

            # Create the product data
            product_data = {
                'BRAND NAME': brand_name,
                'ITEM DESCRIPTION': item_description,
                'COLOR': color,
                'SIZE': size,
                'ORIGINAL QTY': original_qty,
                'ORIGINAL RETAIL PRICE': original_retail_price,
                'IMAGE': image
            }

            # Update or insert the product into the collection
            result = collection_example_lot.update_one(filter, {'$set': product_data}, upsert=True)

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


adidas_collection = db["ADIDAS IN STOCK!"]

class ADIDAS (Resource):
    def post(self):
        try:
            photo = request.form.get('Photo')
            article = request.form.get('Article')
            model = request.form.get('Model')
            size_s = request.form.get('S')
            size_m = request.form.get('M')
            size_l = request.form.get('L')
            size_xl = request.form.get('XL')
            size_xxl = request.form.get('XXL')
            total = request.form.get('Total')
            price = request.form.get('Price')
            rrp = request.form.get('RRP/UVP')

            # Create a filter to check if the product already exists
            filter = {
                'Article': article
            }

            # Create the product data
            # product_data = {
            #     'Photo': photo,
            #     'Article': article,
            #     'Model': model,
            #     'S': size_s,
            #     'M': size_m,
            #     'L': size_l,
            #     'XL': size_xl,
            #     'XXL': size_xxl,
            #     'Total': total,
            #     'Price': price,
            #     'RRP/UVP': rrp
            # }

            product_data = {
                'Photo': photo,
                'Article': article,
                'Model': model,
                'Sizes': {
                    'S': size_s,
                    'M': size_m,
                    'L': size_l,
                    'XL': size_xl,
                    'XXL': size_xxl
                },
                'Total': total,
                'Price': price,
                'RRP/UVP': rrp
            }

            # Update or insert the product into the collection
            result = adidas_collection.update_one(filter, {'$set': product_data}, upsert=True)

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

DNC_WHOLESALE_DISTRIBUTOR_PRICE_LIST_collection = db['DNC WHOLESALE DISTRIBUTOR PRICE LIST']

class DNC_WHOLESALE(Resource):
    def post(self):
        try:
            store = request.form.get('Store')
            lot_number = request.form.get('Lot#')
            category = request.form.get('Merchandise Category')
            quantity = request.form.get('Quantity')
            unit_price = request.form.get('Unit Price In United States Dollars')
            #unit_price = request.form.get('Unit Price In United States Dollars[]')


            product_data = {
                'Store': store,
                'Lot#': lot_number,
                'Merchandise Category': category,
                'Quantity': quantity,
                'Unit Price In United States Dollars': unit_price
            }

            # Define the filter to check if the product already exists
            filter = {
                'Store': store,
                'Lot#': lot_number
            }

            # Update or insert the product into the collection
            result = DNC_WHOLESALE_DISTRIBUTOR_PRICE_LIST_collection.update_one(filter, {'$set': product_data}, upsert=True)

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

XMBO_offerCHARMEX_collection = db['XMBO-offerCHARMEX']

class XMBO_offerCHARMEX(Resource):
    def post(self):
        try:
            picture = request.form.get('Picture')
            ref = request.form.get('REF')
            brand = request.form.get('BRAND')
            description = request.form.get('DESCRIPTION')
            hs = request.form.get('HS')
            material = request.form.get('Material')
            made_in = request.form.get('Made in')
            qty = request.form.get('QTY')
            retail_price = request.form.get('RETAIL PRICE')

            product_data = {
                'Picture': picture,
                'REF': ref,
                'BRAND': brand,
                'DESCRIPTION': description,
                'HS': hs,
                'Material': material,
                'Made in': made_in,
                'QTY': qty,
                'RETAIL PRICE': retail_price
            }

            # Define the filter to check if the product already exists
            filter = {
                'REF': ref
            }

            # Update or insert the product into the collection
            result = XMBO_offerCHARMEX_collection.update_one(filter, {'$set': product_data}, upsert=True)

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

