'''
These will be format of the messages exchanged between 
the publisher and the subscriber.
'''

class Publication(BaseModel):
    message_id: str
    topic: str
    message: dict[str, Any] #Any for now, until we figure out the exact information we want to send
    origin: str
    
class BrokerInfo(BaseModel):
    broker_id: str
    broker_ip: str
    broker_port: int
    peer_brokers: List[str]
    
class Subscription(BaseModel):
    subscriber_id: str
    topic: str
    subscriber_ip: str
    subscriber_port: int
    
class PublishRequest(BaseModel):
    topic: str
    message: dict[str, Any] #Any for now, until we figure out the exact information we want to send
    origin: str