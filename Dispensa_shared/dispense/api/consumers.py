# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from dispense.models import DispensaUser, Dispensa
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class UserShareConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id_user = self.scope['url_route']['kwargs']['id_user']
        await self.channel_layer.group_add(
            f"user_{self.id_user}",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f"user_{self.id_user}",
            self.channel_name
        )
    
    async def user_share_notification(self, event):
        message = event['message']
        color = event['color']
        await self.send(text_data=json.dumps({
            'message': message,
            'color': color
        }))

@receiver(post_save, sender=DispensaUser)
def user_share_saved(sender, instance, **kwargs):
    id_user = instance.id_user
    condivisa_da = instance.condivisa_da

    print(f"{condivisa_da.username} ha condiviso con te la dispensa {instance.id_dispensa}!")

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{id_user}",
        {
            "type": "user_share_notification",
            "color": "add",
            "message": f"{condivisa_da.username} ha condiviso con te la dispensa {instance.id_dispensa}!"
        }
    )

@receiver(post_delete, sender=DispensaUser)
def user_share_deleted(sender, instance, **kwargs):
    id_user = instance.id_user
    condivisa_da = instance.condivisa_da

    print(f"{condivisa_da.username} ha condiviso con te la dispensa {instance.id_dispensa}!")

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{id_user}",
        {
            "type": "user_share_notification",
            "color": "remove",
            "message": f"{condivisa_da.username} ha rimosso la condivisione della dispensa {instance.id_dispensa}!"
        }
    )
