import os

import firebase_admin
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from rest_framework import exceptions

from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .exceptions import NoAuthToken

cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "dispensa-shared",
        "private_key_id": "404d85372095acc6381d7077e5d0184966d03683",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQCHeefgYjqmWrYe\nFldPhJRC4WS9cHJkPNYz7SSIJwClHTgHUgKcIdPH+ELj5/cyyvc23tALra5/Wjl2\nTaTjCvFWksAoEXXcKzfgnA85tjqnrVCgul81rxXqcBO/In2Lpv+y0N/YPX7AdB97\neLe6l5HZl2EgDqVWnCJVSfp2TOOkjmhthkpsWjO/tmI3EZrmlv3FsBxpEfcxlWj5\noLKtFKkR2tEtawSKfUsYD5WE/7Kp2+IFalqn/Xfd3rNaFuzahfZ8c1NjHU0uHgfS\nPycFqTDuz1U+ZWfdOjag/XEpKnRYNp9kSdRDWE5caxottKwDREoVABzSwRR91K0W\ndJENvsRJAgMBAAECgf8uu1VGgPOZVRPf8Z4S7wJaFvu14MkChTRPzsE+d89VQq6E\nPlKkffgRpW7bKzmCY6HYMCv9zKuHciTRix82e20Ykq7IZVq9CvDszV1khX0Y6Jvs\n5CKQ0abGz4b47RM5QyHtNtpmobniVQeVtjw8n1jd9gBSKfz/ewvR2H3xrEAUv0E4\nCJh/qcOh5SQQmaGTZmz9cqruX8q0t3B9UzmHMaDtnOTSuwS1y8X/K+6RtMUjR8F0\n7ldNoyqVznBC5/xy8KWcHhNpVuNIB/bHjiFQu0zvmNMQKlepWe0OnhZb9X8KuhB6\nPt4n2OSi1Ro2cBGEMc5T7kg+A9DLTwlyjgY96uECgYEAv1ocUKx+2AVOVLCv6yCA\nNmI239vhjYDQlfQErJ8aIVXTyRI8B0xm2Y67VCUJWYPPptmtCgqUQDoDbV/FHHIO\nHd/N5qmESBrqT7WqAr6tAnSFtTMscqBqI+dSnywUt+912M33jXYWMBbJ3gYWkc0Z\na8+5q5qhcxcNx7BvwrqE0zkCgYEAtT8jsgKHQDNpZLa82aal5p9fT0o0d4n7LEBK\n1O2vHeD4/ZtZ2zoxyGxP9/7XB3TgyTzB+vmemufqnFDT7FOk2q7Y5v+VoDvrTLxt\nEQW5WweOwZnm6+yXdH/5yr8ZWAT2I9wDSwsLrurBfQs8dj3vtLAunu998tYWzAO0\noJ0nKZECgYEAiqo+Qqf984VE0lKH6RfQUZiys16gAO8MON5wVLenM+kCZH92SMOw\n9I9eaQe90sSWQg8UOmaYMELaIPR53rc4S6XXjAPj/Gykx8aZwQt0TIcsLbc7yoU8\n5W/Ii9hh2zkIaWg4sKaWRZr+Bora6CV8+oe5wQV5YfGe5sqQ8sg/YOECgYBE7n+H\n6xg/XY4+5JUMfinofUKFaGZt9EdXvBf5xW/tgCuSYGwbSZW3cSI04nIrftMjFf18\nk0U0CvIag08mOWWgWhFaQWhJqaBC7gLZD4FAUq6DiSHfJnsvrqB08JsV88UdPEbw\nWoIWA2iVQxm6qrGo2bzRa6pOGghPjTU8RKipUQKBgHdfzj1drAcjdUnBGxAg3bWs\nkMNu04VcQnV931y4Qs5jbiRvJK+SOALLCHkj1F5kIRjanK0HW8W8iVF6uRbIs5wb\nmd8hvuDc8tsdyo937+njvF5+i5qGsaJ7SN3VQyKl7YHlzlHxMusVoNV8aHYnAHQh\nLHQQB0eL+HKtqn51Mfpf\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-kfe3e@dispensa-shared.iam.gserviceaccount.com",
        "client_id": "111315023300718659759",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-kfe3e%40dispensa-shared.iam.gserviceaccount.com",
        
    }
)

#  "type": "service_account",
#         "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
#         "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
#         "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
#         "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
#         "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://accounts.google.com/o/oauth2/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": os.environ.get("FIREBASE_CLIENT_CERT_URL"),

#cred = credentials.Certificate("dispensa-shared-firebase.json")
default_app = firebase_admin.initialize_app(cred)


class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        #xsuser.profile.last_activity = timezone.localtime()

        return (user, None)