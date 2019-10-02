# sendIT-api
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.


#### How should this be manually tested?
- Clone the repository
- Initialize and activate a virtualenv
 ```
 $ virtualenv --no-site-packages env
 $ create db of your choice and edit the .env file to suite your needs
 $ source .env
 ```
- Install the dependencies
 ```
 $ pip install -r requirements.txt
 ```

- Run the development server
```
$ flask run
```
- Navigate to [http://localhost:5000](http://localhost:5000)

- Test all endpoints using postman


## Endpoints

Here is a list of all endpoints

| Endpoint                       | Functionality                 |
| ------------------------------ | ----------------------------- |
| GET   /api/v1/parcels           | Fetch all parcel delivery orders |
| GET   /api/v1/parcels/parelId | Fetch a specific parcel delivery order |
| POST   /api/v1/parcels          | Create a parcel delivery order |
| GET  /api/users/userId/parcels | Fetch all parcel delivery orders by a specific user|
| PUT   /api/v1parcels/parcelId/cancel  | Cancel the specific parcel delivery order  |


## Screenshot demos from Postman

![Alt text](assets/get-sendit-api.png?raw=true "GET Example")
![Alt text](assets/post-sendit-api.png?raw=true "POST EXample")

