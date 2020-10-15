# wazo_appgateway_client.BridgesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bridges_bridge_id_add_channel_post**](BridgesApi.md#bridges_bridge_id_add_channel_post) | **POST** /bridges/{bridgeId}/addChannel | Add a channel to a bridge.
[**bridges_bridge_id_delete**](BridgesApi.md#bridges_bridge_id_delete) | **DELETE** /bridges/{bridgeId} | Shut down a bridge.
[**bridges_bridge_id_get**](BridgesApi.md#bridges_bridge_id_get) | **GET** /bridges/{bridgeId} | Get bridge details.
[**bridges_bridge_id_moh_delete**](BridgesApi.md#bridges_bridge_id_moh_delete) | **DELETE** /bridges/{bridgeId}/moh | Stop playing music on hold to a bridge.
[**bridges_bridge_id_moh_post**](BridgesApi.md#bridges_bridge_id_moh_post) | **POST** /bridges/{bridgeId}/moh | Play music on hold to a bridge or change the MOH class that is playing.
[**bridges_bridge_id_play_playback_id_post**](BridgesApi.md#bridges_bridge_id_play_playback_id_post) | **POST** /bridges/{bridgeId}/play/{playbackId} | Start playback of media on a bridge.
[**bridges_bridge_id_play_post**](BridgesApi.md#bridges_bridge_id_play_post) | **POST** /bridges/{bridgeId}/play | Start playback of media on a bridge.
[**bridges_bridge_id_post**](BridgesApi.md#bridges_bridge_id_post) | **POST** /bridges/{bridgeId} | Create a new bridge or updates an existing one.
[**bridges_bridge_id_record_post**](BridgesApi.md#bridges_bridge_id_record_post) | **POST** /bridges/{bridgeId}/record | Start a recording.
[**bridges_bridge_id_remove_channel_post**](BridgesApi.md#bridges_bridge_id_remove_channel_post) | **POST** /bridges/{bridgeId}/removeChannel | Remove a channel from a bridge.
[**bridges_bridge_id_video_source_channel_id_post**](BridgesApi.md#bridges_bridge_id_video_source_channel_id_post) | **POST** /bridges/{bridgeId}/videoSource/{channelId} | Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
[**bridges_bridge_id_video_source_delete**](BridgesApi.md#bridges_bridge_id_video_source_delete) | **DELETE** /bridges/{bridgeId}/videoSource | Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
[**bridges_get**](BridgesApi.md#bridges_get) | **GET** /bridges | List all active bridges in Asterisk.
[**bridges_post**](BridgesApi.md#bridges_post) | **POST** /bridges | Create a new bridge.


# **bridges_bridge_id_add_channel_post**
> bridges_bridge_id_add_channel_post(bridge_id, channel, role=role, absorb_dtmf=absorb_dtmf, mute=mute, x_asterisk_id=x_asterisk_id)

Add a channel to a bridge.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
channel = ['channel_example'] # list[str] | Ids of channels to add to bridge
role = 'role_example' # str | Channel's role in the bridge (optional)
absorb_dtmf = False # bool | Absorb DTMF coming from this channel, preventing it to pass through to the bridge (optional) (default to False)
mute = False # bool | Mute audio from this channel, preventing it to pass through to the bridge (optional) (default to False)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Add a channel to a bridge.
        api_instance.bridges_bridge_id_add_channel_post(bridge_id, channel, role=role, absorb_dtmf=absorb_dtmf, mute=mute, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_add_channel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **channel** | [**list[str]**](str.md)| Ids of channels to add to bridge | 
 **role** | **str**| Channel&#39;s role in the bridge | [optional] 
 **absorb_dtmf** | **bool**| Absorb DTMF coming from this channel, preventing it to pass through to the bridge | [optional] [default to False]
 **mute** | **bool**| Mute audio from this channel, preventing it to pass through to the bridge | [optional] [default to False]
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_delete**
> bridges_bridge_id_delete(bridge_id, x_asterisk_id=x_asterisk_id)

Shut down a bridge.

If any channels are in this bridge, they will be removed and resume whatever they were doing beforehand.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Shut down a bridge.
        api_instance.bridges_bridge_id_delete(bridge_id, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_get**
> Bridge bridges_bridge_id_get(bridge_id, x_asterisk_id=x_asterisk_id)

Get bridge details.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Get bridge details.
        api_response = api_instance.bridges_bridge_id_get(bridge_id, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Bridge**](Bridge.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_moh_delete**
> bridges_bridge_id_moh_delete(bridge_id, x_asterisk_id=x_asterisk_id)

Stop playing music on hold to a bridge.

This will only stop music on hold being played via POST bridges/{bridgeId}/moh.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Stop playing music on hold to a bridge.
        api_instance.bridges_bridge_id_moh_delete(bridge_id, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_moh_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_moh_post**
> bridges_bridge_id_moh_post(bridge_id, moh_class=moh_class, x_asterisk_id=x_asterisk_id)

Play music on hold to a bridge or change the MOH class that is playing.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
moh_class = 'moh_class_example' # str | Channel's id (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Play music on hold to a bridge or change the MOH class that is playing.
        api_instance.bridges_bridge_id_moh_post(bridge_id, moh_class=moh_class, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_moh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **moh_class** | **str**| Channel&#39;s id | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_play_playback_id_post**
> Playback bridges_bridge_id_play_playback_id_post(bridge_id, playback_id, media, lang=lang, offsetms=offsetms, skipms=skipms, x_asterisk_id=x_asterisk_id)

Start playback of media on a bridge.

The media URI may be any of a number of URI's. Currently sound:, recording:, number:, digits:, characters:, and tone: URI's are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
playback_id = 'playback_id_example' # str | Playback ID.
media = ['media_example'] # list[str] | Media URIs to play.
lang = 'lang_example' # str | For sounds, selects language for sound. (optional)
offsetms = 0 # int | Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. (optional) (default to 0)
skipms = 3000 # int | Number of milliseconds to skip for forward/reverse operations. (optional) (default to 3000)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Start playback of media on a bridge.
        api_response = api_instance.bridges_bridge_id_play_playback_id_post(bridge_id, playback_id, media, lang=lang, offsetms=offsetms, skipms=skipms, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_play_playback_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **playback_id** | **str**| Playback ID. | 
 **media** | [**list[str]**](str.md)| Media URIs to play. | 
 **lang** | **str**| For sounds, selects language for sound. | [optional] 
 **offsetms** | **int**| Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. | [optional] [default to 0]
 **skipms** | **int**| Number of milliseconds to skip for forward/reverse operations. | [optional] [default to 3000]
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Playback**](Playback.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_play_post**
> Playback bridges_bridge_id_play_post(bridge_id, media, lang=lang, offsetms=offsetms, skipms=skipms, playback_id=playback_id, x_asterisk_id=x_asterisk_id)

Start playback of media on a bridge.

The media URI may be any of a number of URI's. Currently sound:, recording:, number:, digits:, characters:, and tone: URI's are supported. This operation creates a playback resource that can be used to control the playback of media (pause, rewind, fast forward, etc.)

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
media = ['media_example'] # list[str] | Media URIs to play.
lang = 'lang_example' # str | For sounds, selects language for sound. (optional)
offsetms = 0 # int | Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. (optional) (default to 0)
skipms = 3000 # int | Number of milliseconds to skip for forward/reverse operations. (optional) (default to 3000)
playback_id = 'playback_id_example' # str | Playback Id. (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Start playback of media on a bridge.
        api_response = api_instance.bridges_bridge_id_play_post(bridge_id, media, lang=lang, offsetms=offsetms, skipms=skipms, playback_id=playback_id, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_play_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **media** | [**list[str]**](str.md)| Media URIs to play. | 
 **lang** | **str**| For sounds, selects language for sound. | [optional] 
 **offsetms** | **int**| Number of milliseconds to skip before playing. Only applies to the first URI if multiple media URIs are specified. | [optional] [default to 0]
 **skipms** | **int**| Number of milliseconds to skip for forward/reverse operations. | [optional] [default to 3000]
 **playback_id** | **str**| Playback Id. | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Playback**](Playback.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_post**
> Bridge bridges_bridge_id_post(bridge_id, type=type, name=name, x_asterisk_id=x_asterisk_id)

Create a new bridge or updates an existing one.

This bridge persists until it has been shut down, or Asterisk has been shut down.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Unique ID to give to the bridge being created.
type = 'type_example' # str | Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu) to set. (optional)
name = 'name_example' # str | Set the name of the bridge. (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Create a new bridge or updates an existing one.
        api_response = api_instance.bridges_bridge_id_post(bridge_id, type=type, name=name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Unique ID to give to the bridge being created. | 
 **type** | **str**| Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu) to set. | [optional] 
 **name** | **str**| Set the name of the bridge. | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Bridge**](Bridge.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_record_post**
> LiveRecording bridges_bridge_id_record_post(bridge_id, name, format, max_duration_seconds=max_duration_seconds, max_silence_seconds=max_silence_seconds, if_exists=if_exists, beep=beep, terminate_on=terminate_on, x_asterisk_id=x_asterisk_id)

Start a recording.

This records the mixed audio from all channels participating in this bridge.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
name = 'name_example' # str | Recording's filename
format = 'format_example' # str | Format to encode audio in
max_duration_seconds = 0 # int | Maximum duration of the recording, in seconds. 0 for no limit. (optional) (default to 0)
max_silence_seconds = 0 # int | Maximum duration of silence, in seconds. 0 for no limit. (optional) (default to 0)
if_exists = 'fail' # str | Action to take if a recording with the same name already exists. (optional) (default to 'fail')
beep = False # bool | Play beep when recording begins (optional) (default to False)
terminate_on = 'none' # str | DTMF input to terminate recording. (optional) (default to 'none')
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Start a recording.
        api_response = api_instance.bridges_bridge_id_record_post(bridge_id, name, format, max_duration_seconds=max_duration_seconds, max_silence_seconds=max_silence_seconds, if_exists=if_exists, beep=beep, terminate_on=terminate_on, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_record_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **name** | **str**| Recording&#39;s filename | 
 **format** | **str**| Format to encode audio in | 
 **max_duration_seconds** | **int**| Maximum duration of the recording, in seconds. 0 for no limit. | [optional] [default to 0]
 **max_silence_seconds** | **int**| Maximum duration of silence, in seconds. 0 for no limit. | [optional] [default to 0]
 **if_exists** | **str**| Action to take if a recording with the same name already exists. | [optional] [default to &#39;fail&#39;]
 **beep** | **bool**| Play beep when recording begins | [optional] [default to False]
 **terminate_on** | **str**| DTMF input to terminate recording. | [optional] [default to &#39;none&#39;]
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**LiveRecording**](LiveRecording.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_remove_channel_post**
> bridges_bridge_id_remove_channel_post(bridge_id, channel, x_asterisk_id=x_asterisk_id)

Remove a channel from a bridge.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
channel = ['channel_example'] # list[str] | Ids of channels to remove from bridge
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Remove a channel from a bridge.
        api_instance.bridges_bridge_id_remove_channel_post(bridge_id, channel, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_remove_channel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **channel** | [**list[str]**](str.md)| Ids of channels to remove from bridge | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_video_source_channel_id_post**
> bridges_bridge_id_video_source_channel_id_post(bridge_id, channel_id, x_asterisk_id=x_asterisk_id)

Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
channel_id = 'channel_id_example' # str | Channel's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
        api_instance.bridges_bridge_id_video_source_channel_id_post(bridge_id, channel_id, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_video_source_channel_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **channel_id** | **str**| Channel&#39;s id | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_bridge_id_video_source_delete**
> bridges_bridge_id_video_source_delete(bridge_id, x_asterisk_id=x_asterisk_id)

Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    bridge_id = 'bridge_id_example' # str | Bridge's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
        api_instance.bridges_bridge_id_video_source_delete(bridge_id, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_bridge_id_video_source_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bridge_id** | **str**| Bridge&#39;s id | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_get**
> list[Bridge] bridges_get(x_asterisk_id=x_asterisk_id)

List all active bridges in Asterisk.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List all active bridges in Asterisk.
        api_response = api_instance.bridges_get(x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[Bridge]**](Bridge.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bridges_post**
> Bridge bridges_post(type=type, bridge_id=bridge_id, name=name, x_asterisk_id=x_asterisk_id)

Create a new bridge.

This bridge persists until it has been shut down, or Asterisk has been shut down.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.BridgesApi(api_client)
    type = 'type_example' # str | Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu). (optional)
bridge_id = 'bridge_id_example' # str | Unique ID to give to the bridge being created. (optional)
name = 'name_example' # str | Name to give to the bridge being created. (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Create a new bridge.
        api_response = api_instance.bridges_post(type=type, bridge_id=bridge_id, name=name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BridgesApi->bridges_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Comma separated list of bridge type attributes (mixing, holding, dtmf_events, proxy_media, video_sfu). | [optional] 
 **bridge_id** | **str**| Unique ID to give to the bridge being created. | [optional] 
 **name** | **str**| Name to give to the bridge being created. | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Bridge**](Bridge.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

