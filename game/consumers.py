import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs

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
        if len(count) > 3:
            # await self.send(text_data=json.dumps(message))
            self.playing_as = 'B'
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'remove_onboarding',
                    'onboarding_state_value': False,
                }
            )

    

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
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'gameroom_message',
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