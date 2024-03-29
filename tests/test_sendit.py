import unittest
import os
import json
from app import create_app, db


class SendItTestCase(unittest.TestCase):
    """This class represents the sendit test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.sendit = {'name': 'test_parcel'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_parcel_creation(self):
        """Test API can create a parcel (POST request)"""
        res = self.client().post('/parcels/', data=self.sendit)
        self.assertEqual(res.status_code, 201)
        self.assertIn('test_parcel', str(res.data))

    def test_api_can_get_all_parcels(self):
        """Test API can get a parcel (GET request)."""
        res = self.client().post('/parcels/', data=self.sendit)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/parcels/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('test_parcel', str(res.data))

    def test_api_can_get_parcel_by_id(self):
        """Test API can get a single parcel by using it's id."""
        rv = self.client().post('/parcels/', data=self.sendit)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/parcels/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('test_parcel', str(result.data))

    def test_parcel_can_be_edited(self):
        """Test API can edit an existing parcel. (PUT request)"""
        rv = self.client().post(
            '/parcels/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/parcels/1',
            data={
                "name": "Dont just eat, but also pray and love :-)"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/parcels/1')
        self.assertIn('Dont just eat', str(results.data))

    def test_parcel_deletion(self):
        """Test API can delete an existing parcel. (DELETE request)."""
        rv = self.client().post(
            '/parcels/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/parcels/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/parcels/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()