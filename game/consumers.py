import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from urllib.parse import parse_qs
from .models import Mapper
from core.models import User

class GameRoomConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.players = {}

    async def connect(self): 
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        
        query_params = parse_qs(self.scope['query_string'].decode())
        self.username = query_params.get('username', [None])[0]
        
        
        print(query_params.get('username', [None])[0])
        self.room_group_name = 'chat_%s' % self.room_name

        if self.room_name == 'undefined' or self.username=='undefined':
            return
        
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        print("---------------")
        print(self.channel_layer.groups.get('baghchal',{}))
        print(len(self.channel_layer.groups.get(self.room_group_name, {}).items()))

        await self.accept()

        self.players[self.channel_name] = self.username
        print(self.players)
        # Get all the channel names in the group
        # players = self.channel_layer.group_channels(self.room_group_name)
        # print(players)
        # Retrieve the usernames of the players from the channel names
        # print([channel.name.split('.')[-1] for channel in players])
        # await self.accept({'another_player': self.username})

        # Check if there are two players in the room
        count = self.channel_layer.groups.get(self.room_group_name, {}).items()
        # first_user_channel = list(self.channel_layer.groups[self.room_group_name])[0]
        # print(111, first_user_channel)
        # first_user = await self.channel_layer.receive(first_user_channel)
        # print(222,first_user)
        # if(self.username != 'undefined'):
        #     print(555555, self.username)
        if len(count) == 1 and self.username != 'undefined' and self.room_name != 'undefined':
            def runIt():
                (mapper,created) = Mapper.objects.get_or_create(room=self.room_name)
                if created:
                    user = User.objects.get(username= self.username)
                    mapper.player1 = user
                    print("*********************888 Mapper Run")
                    print(self.room_group_name)
                    mapper.save()
            await sync_to_async(runIt)()

        if len(count) == 2 and self.username != 'undefined' and self.room_name != 'undefined':
            # await self.send(text_data=json.dumps(message))
            def runIt():
                (mapper,created) = Mapper.objects.get_or_create(room=self.room_name)
                print(self.username)
                user = User.objects.get(username=self.username)
                mapper.player2 = user
                mapper.save()
            await sync_to_async(runIt)()
            # await self.send(text_data=json.dumps(message))
            self.playing_as = 'B'
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'remove_onboarding',
                    'onboarding_state_value': False,
                }
            )
            print('Onboarding hatena')

    

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'tester_message',
        #         'tester': 'hello world',
        #     }
        # )

    # async def tester_message(self, event):
    #     tester = event['tester']
    #     await self.send(text_data = json.dumps({
    #         'tester': tester,
    #     }))
    
    async def remove_onboarding(self, event):
        typ = event['type']
        value = event['onboarding_state_value']
        await self.send(text_data = json.dumps({
            'type': typ,
            'value': value,
        }))

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        if text_data_json['type'] == 'message':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'gameroom_message',
                    'message': message,
                    'username': username,
                }
            )

        if text_data_json['type'] == 'chatmessage':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chatroom_message',
                    'message': message,
                    'username': username,
                }
            )

    async def gameroom_message(self, event):
        typ = event['type']
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'type': typ,
            'message': message,
            'username': username,
        }))

    async def chatroom_message(self, event):
        typ = event['type']
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'type': typ,
            'message': message,
            'username': username,
        }))