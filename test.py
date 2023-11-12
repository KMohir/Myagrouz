from aiogram import Bot, Dispatcher, types

# Initialize your bot and dispatcher

# Your long message
long_message = "This is a very long message that exceeds the character limit..."

# Split the message into smaller chunks
message_chunks = [long_message[i:i + 4000] for i in range(0, len(long_message), 4000)]

# Send each chunk as a separate message
for chunk in message_chunks:
    print(chunk)