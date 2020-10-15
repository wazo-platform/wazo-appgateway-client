# wazo_appgateway_client.EventsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_get**](EventsApi.md#events_get) | **GET** /events | WebSocket connection for events.
[**events_user_event_name_post**](EventsApi.md#events_user_event_name_post) | **POST** /events/user/{eventName} | Generate a user event.


# **events_get**
> Message events_get(app, subscribe_all=subscribe_all, x_asterisk_id=x_asterisk_id)

WebSocket connection for events.

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
    api_instance = wazo_appgateway_client.EventsApi(api_client)
    app = ['app_example'] # list[str] | Applications to subscribe to.
subscribe_all = True # bool | Subscribe to all Asterisk events. If provided, the applications listed will be subscribed to all events, effectively disabling the application specific subscriptions. Default is 'false'. (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # WebSocket connection for events.
        api_response = api_instance.events_get(app, subscribe_all=subscribe_all, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app** | [**list[str]**](str.md)| Applications to subscribe to. | 
 **subscribe_all** | **bool**| Subscribe to all Asterisk events. If provided, the applications listed will be subscribed to all events, effectively disabling the application specific subscriptions. Default is &#39;false&#39;. | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Message**](Message.md)

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

# **events_user_event_name_post**
> events_user_event_name_post(event_name, application, source=source, x_asterisk_id=x_asterisk_id, containers=containers)

Generate a user event.

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
    api_instance = wazo_appgateway_client.EventsApi(api_client)
    event_name = 'event_name_example' # str | Event name
application = 'application_example' # str | The name of the application that will receive this event
source = ['source_example'] # list[str] | URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}/{resource}, deviceState:{deviceName} (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)
containers = wazo_appgateway_client.Containers() # Containers | The \"variables\" key in the body object holds custom key/value pairs to add to the user event. Ex. { \"variables\": { \"key\": \"value\" } } (optional)

    try:
        # Generate a user event.
        api_instance.events_user_event_name_post(event_name, application, source=source, x_asterisk_id=x_asterisk_id, containers=containers)
    except ApiException as e:
        print("Exception when calling EventsApi->events_user_event_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **str**| Event name | 
 **application** | **str**| The name of the application that will receive this event | 
 **source** | [**list[str]**](str.md)| URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}/{resource}, deviceState:{deviceName} | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 
 **containers** | [**Containers**](Containers.md)| The \&quot;variables\&quot; key in the body object holds custom key/value pairs to add to the user event. Ex. { \&quot;variables\&quot;: { \&quot;key\&quot;: \&quot;value\&quot; } } | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

