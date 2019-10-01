from flask import Blueprint, request, abort, jsonify

from ..models.models import * 

api = Blueprint('api', __name__)

@api.route('/parcels/', methods=['GET', 'POST'])
def get_all_parcels():
    # Retrieve all parcels
    if request.method == "POST":
        name = str(request.data.get('name', ''))
        if name:
            parcel = Parcel(
                
            )
            parcel.save()
            response = jsonify({
                'id': parcel.id,
                'name': parcel.name,
                'date_created': parcel.date_created,
                'date_modified': parcel.date_modified
            })
            response.status_code = 201
            return response
    

    return("{You've Got all parcels}")

@api.route('/parcels/<int:parcel_id>/', methods=['GET'])
def get_specific_parcel(parcel_id):
    return("{You've Got one parcel}")

@api.route('/users/<int:user_id>/parcels/', methods=['GET'])
def get_user_parcels(user_id):
    return("{You've Got user parcels}")

@api.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_parcel(parcel_id):
    return("{You've cancelled a parcel}")