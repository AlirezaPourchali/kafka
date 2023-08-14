from kafka import KafkaConsumer
import sys

consumer = KafkaConsumer('mmd',
#                         group_id=None,
                         bootstrap_servers=['localhost:29092'], auto_offset_reset='earliest' , enable_auto_commit=False)

#consumer.seek_to_beginning("Partition0")
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print (message.value)


