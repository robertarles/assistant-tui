#!/usr/bin/env python3
import json

from openai import OpenAI

client = OpenAI()

assistantName = "hiro"
assistantID = "asst_vVjkIX5UzTyGROBG1fj6Lmkz"
threadID = "thread_ufYt3oNUn8dnqAP4lobD5zZp"

my_assistant = client.beta.assistants.retrieve(assistantID)
# Debug. Colored and formatted print of my_assistant
# pretty print the assistant
print(json.dumps(my_assistant.model_dump_json(), indent=4, sort_keys=True))
