from dicttoxml import dicttoxml
from flask import Blueprint, request, jsonify

from ..models.models import User, Parcel

api = Blueprint('api', __name__)


@api.route('/parcels/', methods=['GET', 'POST'])
def parcels():

    if request.method == "POST":
        # POST
        # Gets name argument variable from url
        name = request.args.get('name')
        user_id = request.args.get('sender')
        user_location = request.args.get('location')
        destination = request.args.get('dest')
        parc_weight = request.args.get('parc_weight')

        if name:
            parcel = Parcel(
                name=name,
                senderId=user_id,
                delivered=False,
                presentLocation=user_location,
                pickupLocation=None,
                destination=destination,
                parcelWeight=parc_weight
            )
            parcel.save()

            response = {
                'parcelId': parcel.id,
                'parcelName': parcel.name,
                'sender': User.query.filter(User.id == user_id).first().name,
                'delivered': parcel.delivered,
                'presentLocation': parcel.presentLocation,
                'pickupLocation': parcel.pickupLocation,
                'destination': parcel.destination,
                'parcelWeight': parcel.parcelWeight
            }

            response = dicttoxml(response, custom_root='test', attr_type=False)

            # response.status_code = 201
            return response

    else:
        # GET
        all_parcels = Parcel.get_all()
        results = []

        for parcel in all_parcels:
            obj = {
                'parcelId': parcel.id,
                'parcelName': parcel.name,
                'sender': User.query.filter(User.id == parcel.senderId).first().name,
                'delivered': parcel.delivered,
                'presentLocation': parcel.presentLocation,
                'pickupLocation': parcel.pickupLocation,
                'destination': parcel.destination,
                'parcelWeight': parcel.parcelWeight
            }

            results.append(obj)

        response = dicttoxml(results, custom_root='test', attr_type=False)
        # response.status_code = 200
        return response


@api.route('/parcels/<int:parcel_id>/', methods=['GET'])
def get_specific_parcel(parcel_id):
    # GET
    parcel = Parcel.query.filter(Parcel.id==parcel_id).first_or_404()
    results = []

    obj = {
        'parcelId': parcel.id,
        'parcelName': parcel.name,
        'sender': User.query.filter(User.id == Parcel.senderId).first().name,
        'delivered': parcel.delivered,
        'presentLocation': parcel.presentLocation,
        'pickupLocation': parcel.pickupLocation,
        'destination': parcel.destination,
        'parcelWeight': parcel.parcelWeight
    }

    results.append(obj)

    response = dicttoxml(results, custom_root='test', attr_type=False)
    # response.status_code = 200
    return response


@api.route('/users/<int:user_id>/parcels/', methods=['GET'])
def get_user_parcels(user_id):

    parcels = Parcel.query.filter(Parcel.senderId==user_id)
    results = []

    for parcel in parcels:
        obj = {
            'parcelId': parcel.id,
            'parcelName': parcel.name,
            'sender': User.query.filter(User.id == user_id).first().name,
            'delivered': parcel.delivered,
            'presentLocation': parcel.presentLocation,
            'pickupLocation': parcel.pickupLocation,
            'destination': parcel.destination,
            'parcelWeight': parcel.parcelWeight
        }

        results.append(obj)

    response = dicttoxml(results, custom_root='test', attr_type=False)
    # response.status_code = 200
    return response


@api.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_parcel(parcel_id):

    parcel = Parcel.query.filter(Parcel.senderId==parcel_id).first_or_404()
    results = []

    obj = {
        'parcelId': parcel.id,
        'parcelName': parcel.name,
        'sender': User.query.filter(User.id == parcel.id).first().name,
        'delivered': parcel.delivered,
        'presentLocation': parcel.presentLocation,
        'pickupLocation': parcel.pickupLocation,
        'destination': parcel.destination,
        'parcelWeight': parcel.parcelWeight
    }

    parcel.delete()

    results.append(obj)

    response = dicttoxml(results, custom_root='test', attr_type=False)
    response.status_code = 200
    return response


@api.route('/users/', methods=['GET', 'POST'])
def users():

    if request.method == "POST":
        # POST
        # Gets name argument variable from url
        name = request.args.get('name')
        email = request.args.get('email')
        phone = request.args.get('phone')

        if name:
            user = User(
                name=name,
                email=email,
                mobileNo=phone,
                isAdmin=0
            )
            user.save()

            response = {
                'userId': user.id,
                'userName': user.name,
                'email': user.email,
                'mobileNo': user.mobileNo,
            }

            response = dicttoxml(response, custom_root='test', attr_type=False)

            # response.status_code = 201
            return response

    else:
        # GET
        all_users = User.get_all()
        results = []

        for user in all_users:
            obj = {
                'userId': user.id,
                'userName': user.name,
                'email': user.email,
                'mobileNo': user.mobileNo,
            }

            results.append(obj)

        response = dicttoxml(results, custom_root='test', attr_type=False)
        # response.status_code = 200
        return response