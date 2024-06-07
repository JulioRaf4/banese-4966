import asyncio
import os
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
from azure.identity.aio import DefaultAzureCredential
import logging

NAMESPACE_CONNECTION_STR = os.getenv("NAMESPACE_CONNECTION_STR")
QUEUE_NAME = "fila_teste_4966"


async def send_single_message(sender, msg):
    # Create a Service Bus message and send it to the queue
    message = ServiceBusMessage(msg)
    await sender.send_messages(message)


async def send_a_list_of_messages(sender):
    # Create a list of messages and send it to the queue
    messages = [ServiceBusMessage("Message in list") for _ in range(5)]
    await sender.send_messages(messages)
    print("Sent a list of 5 messages")


async def send_batch_message(sender):
    # Create a batch of messages
    async with sender:
        batch_message = await sender.create_message_batch()
        for _ in range(10):
            try:
                # Add a message to the batch
                batch_message.add_message(
                    ServiceBusMessage("Message inside a ServiceBusMessageBatch")
                )
            except ValueError:
                # ServiceBusMessageBatch object reaches max_size.
                # New ServiceBusMessageBatch object can be created here to send more data.
                break
        # Send the batch of messages to the queue
        await sender.send_messages(batch_message)
    print("Sent a batch of 10 messages")


async def send_messages(msg):
    # create a Service Bus client using the connection string
    try:
        async with ServiceBusClient.from_connection_string(
            conn_str=NAMESPACE_CONNECTION_STR, logging_enable=True
        ) as servicebus_client:
            # Get a Queue Sender object to send messages to the queue
            sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
            async with sender:
                # Send one message
                await send_single_message(sender, msg)
                # Send a list of messages
    except Exception as e:
        logging.warning("ERRO AO CONECTAR COM SERVICE BUS. ")
        pass


async def received_messages():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR, logging_enable=True
    ) as servicebus_client:

        async with servicebus_client:
            # get the Queue Receiver object for the queue
            receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME)
            async with receiver:
                received_msgs = await receiver.receive_messages(
                    max_wait_time=5, max_message_count=20
                )
                for msg in received_msgs:
                    print("Received: " + str(msg))
                    # complete the message so that the message is removed from the queue
                    await receiver.complete_message(msg)
