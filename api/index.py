import requests
# import json

url = "https://sandbox.cashfree.com/pg/orders/sessions"
body = {
        "payment_method": {
            "upi": {
                "channel": "collect ",
                "upi_id": "testtpvfail@gocash",
                "upi_redirect_url": True,
                "upi_expiry_minutes": 10
            }
        },
        "payment_session_id": "session_dbsZETKGl2MIqM9x12CM_yuIsCshv4ABJladS3eE5t8QabuAKTClOytp5L_PAEkCP-9kwKFp1lE6NIcSIenA6hC7dK2gP1jcFH_maDDvd_Fm"
    }
headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-version": "2023-08-01",
        "x-client-id": "TEST425000f78db163221d221dbd07000524",
        "x-client-secret": "TESTd020dacb6239e76cd735c41e9f460f5119616c81"
    }
response = requests.post(url, headers=headers, json=body)
print(f"Response Status Code: {response.status_code}")
print(f"Response Data: {response.text}")
