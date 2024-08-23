import requests
# import json

def fun():
    url = "https://api-preprod.phonepe.com/apis/pg-sandbox/pg/v1/pay"
    payload = {
        "merchantId": "MERCHANTUAT",
        "merchantTransactionId": "OD620471739210623",
        "merchantUserId": "MUID123",
        "amount": 10000,
        "callbackUrl": "https://mykewlapp.com/callback",
        "mobileNumber": "9999999999",
        "paymentInstrument": {
            "type": "UPI_COLLECT",
            "vpa": "test-vpa@ybl"
        }
    }
    headers = {
        "accept": "text/plain",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


def func():
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
    # import requests