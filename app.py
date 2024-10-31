# app.py

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from data import sports_items, item_details
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class ItemList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "success",
            "count": len(sports_items),
            "items": sports_items
        }

class ItemDetail(Resource):
    def get(self, item_id):
        if item_id in item_details:
            return {
                "error": False,
                "message": "success",
                "item": item_details[item_id]
            }
        return {"error": True, "message": "Item not found"}, 404

class ItemSearch(Resource):
    def get(self):
        query = request.args.get('q', '').lower()
        result = [item for item in sports_items if query in item['name'].lower() or query in item['description'].lower()]
        return {
            "error": False,
            "found": len(result),
            "items": result
        }

class AddReview(Resource):
    def post(self):
        data = request.get_json()
        item_id = data.get('id')
        name = data.get('name')
        review = data.get('review')
        
        if item_id in item_details:
            new_review = {
                "name": name,
                "review": review,
                "date": datetime.now().strftime("%d %B %Y")
            }
            item_details[item_id]['customerReviews'].append(new_review)
            return {
                "error": False,
                "message": "Review added successfully",
                "customerReviews": item_details[item_id]['customerReviews']
            }
        return {"error": True, "message": "Item not found"}, 404

class UpdateReview(Resource):
    def put(self):
        data = request.get_json()
        item_id = data.get('id')
        name = data.get('name')
        new_review_text = data.get('review')
        
        if item_id in item_details:
            reviews = item_details[item_id]['customerReviews']
            review_to_update = next((r for r in reviews if r['name'] == name), None)
            if review_to_update:
                review_to_update['review'] = new_review_text
                review_to_update['date'] = datetime.now().strftime("%d %B %Y")
                return {
                    "error": False,
                    "message": "Review updated successfully",
                    "customerReviews": reviews
                }
            return {"error": True, "message": "Review not found"}, 404
        return {"error": True, "message": "Item not found"}, 404

class DeleteReview(Resource):
    def delete(self):
        data = request.get_json()
        item_id = data.get('id')
        name = data.get('name')
        
        if item_id in item_details:
            reviews = item_details[item_id]['customerReviews']
            review_to_delete = next((r for r in reviews if r['name'] == name), None)
            if review_to_delete:
                reviews.remove(review_to_delete)
                return {
                    "error": False,
                    "message": "Review deleted successfully",
                    "customerReviews": reviews
                }
            return {"error": True, "message": "Review not found"}, 404
        return {"error": True, "message": "Item not found"}, 404

# Menambahkan resource ke API
api.add_resource(ItemList, '/list')
api.add_resource(ItemDetail, '/detail/<string:item_id>')
api.add_resource(ItemSearch, '/search')
api.add_resource(AddReview, '/review')
api.add_resource(UpdateReview, '/review/update')
api.add_resource(DeleteReview, '/review/delete')

if __name__ == '__main__':
    app.run(debug=True)
