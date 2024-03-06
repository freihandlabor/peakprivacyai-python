# Api token

Types:

```python
from ppai import ApiTokenValid, ApiTokenNotFoundError
```

Methods:

- <code title="post/ ai/ping">client.chat.<a href="./ppai/resources/chat.py">
  check_api_token</a>() -> <a href="./ppai/types/api_token_valid.py">ApiTokenValid</a></code>

# Models

Types:

```python
from ppai import ModelList, Model
```

Methods:

- <code title="post /completions">client.models.<a href="./ppai/resources/models.py">
  list</a>() -> <a href="./ppai/types/model_list.py">ModelList</a></code>

# Completions

Types:

```python
from ppai import ChatCompletion, Choice, ChatCompletionMessage, CompletionUsage
```

Methods:

- <code title="post /completions">client.chat.completions.<a href="./ppai/resources/completions.py">
  create</a>(\*\*<a href="./ppai/resources/completions.py">
  params</a>) -> <a href="./ppai/types/chat_completion.py">ChatCompletion</a></code>

# Completions Stream

Types:

```python
from ppai import Stream, ChatCompletionChunk, StreamChoice, ChoiceDelta
```

Methods:

- <code title="post /completions">client.chat.completions.<a href="./ppai/resources/completions.py">
  create</a>(\*\*<a href="./ppai/resources/completions.py">
  params</a>) -> <a href="./ppai/types/stream.py">Stream</a></code>
