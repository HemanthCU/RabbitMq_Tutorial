#!/usr/bin/env python
import pika

import os
hostname= os.environ['RABBIT_HOST'] if 'RABBIT_HOST' in os.environ else 'localhost'

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=hostname))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
