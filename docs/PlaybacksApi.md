# wazo_appgateway_client.PlaybacksApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playbacks_playback_id_control_post**](PlaybacksApi.md#playbacks_playback_id_control_post) | **POST** /playbacks/{playbackId}/control | Control a playback.
[**playbacks_playback_id_delete**](PlaybacksApi.md#playbacks_playback_id_delete) | **DELETE** /playbacks/{playbackId} | Stop a playback.
[**playbacks_playback_id_get**](PlaybacksApi.md#playbacks_playback_id_get) | **GET** /playbacks/{playbackId} | Get a playback&#39;s details.


# **playbacks_playback_id_control_post**
> playbacks_playback_id_control_post(playback_id, operation, x_asterisk_id=x_asterisk_id)

Control a playback.

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
    api_instance = wazo_appgateway_client.PlaybacksApi(api_client)
    playback_id = 'playback_id_example' # str | Playback's id
operation = 'operation_example' # str | Operation to perform on the playback.
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Control a playback.
        api_instance.playbacks_playback_id_control_post(playback_id, operation, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling PlaybacksApi->playbacks_playback_id_control_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| Playback&#39;s id | 
 **operation** | **str**| Operation to perform on the playback. | 
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

# **playbacks_playback_id_delete**
> playbacks_playback_id_delete(playback_id, x_asterisk_id=x_asterisk_id)

Stop a playback.

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
    api_instance = wazo_appgateway_client.PlaybacksApi(api_client)
    playback_id = 'playback_id_example' # str | Playback's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Stop a playback.
        api_instance.playbacks_playback_id_delete(playback_id, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling PlaybacksApi->playbacks_playback_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| Playback&#39;s id | 
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

# **playbacks_playback_id_get**
> Playback playbacks_playback_id_get(playback_id, x_asterisk_id=x_asterisk_id)

Get a playback's details.

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
    api_instance = wazo_appgateway_client.PlaybacksApi(api_client)
    playback_id = 'playback_id_example' # str | Playback's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Get a playback's details.
        api_response = api_instance.playbacks_playback_id_get(playback_id, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybacksApi->playbacks_playback_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| Playback&#39;s id | 
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

