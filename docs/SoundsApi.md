# wazo_appgateway_client.SoundsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sounds_get**](SoundsApi.md#sounds_get) | **GET** /sounds | List all sounds.
[**sounds_sound_id_get**](SoundsApi.md#sounds_sound_id_get) | **GET** /sounds/{soundId} | Get a sound&#39;s details.


# **sounds_get**
> list[Sound] sounds_get(lang=lang, format=format, x_asterisk_id=x_asterisk_id)

List all sounds.

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
    api_instance = wazo_appgateway_client.SoundsApi(api_client)
    lang = 'lang_example' # str | Lookup sound for a specific language. (optional)
format = 'format_example' # str | Lookup sound in a specific format. (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List all sounds.
        api_response = api_instance.sounds_get(lang=lang, format=format, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SoundsApi->sounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| Lookup sound for a specific language. | [optional] 
 **format** | **str**| Lookup sound in a specific format. | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[Sound]**](Sound.md)

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

# **sounds_sound_id_get**
> Sound sounds_sound_id_get(sound_id, x_asterisk_id=x_asterisk_id)

Get a sound's details.

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
    api_instance = wazo_appgateway_client.SoundsApi(api_client)
    sound_id = 'sound_id_example' # str | Sound's id
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Get a sound's details.
        api_response = api_instance.sounds_sound_id_get(sound_id, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SoundsApi->sounds_sound_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sound_id** | **str**| Sound&#39;s id | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Sound**](Sound.md)

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

