# wazo_appgateway_client.ApplicationsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_application_name_event_filter_put**](ApplicationsApi.md#applications_application_name_event_filter_put) | **PUT** /applications/{applicationName}/eventFilter | Filter application events types.
[**applications_application_name_get**](ApplicationsApi.md#applications_application_name_get) | **GET** /applications/{applicationName} | Get details of an application.
[**applications_application_name_subscription_delete**](ApplicationsApi.md#applications_application_name_subscription_delete) | **DELETE** /applications/{applicationName}/subscription | Unsubscribe an application from an event source.
[**applications_application_name_subscription_post**](ApplicationsApi.md#applications_application_name_subscription_post) | **POST** /applications/{applicationName}/subscription | Subscribe an application to a event source.
[**applications_get**](ApplicationsApi.md#applications_get) | **GET** /applications | List all applications.


# **applications_application_name_event_filter_put**
> Application applications_application_name_event_filter_put(application_name, x_asterisk_id=x_asterisk_id, body=body)

Filter application events types.

Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:<br /><br />\"allowed\" - Specifies an allowed list of event types<br />\"disallowed\" - Specifies a disallowed list of event types<br /><br />Further, each of those key's value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:<br /><br />\"type\" - The type name of the event to filter<br /><br />The value must be the string name (case sensitive) of the event type that needs filtering. For example:<br /><br />{ \"allowed\": [ { \"type\": \"StasisStart\" }, { \"type\": \"StasisEnd\" } ] }<br /><br />As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.<br /><br />The following rules apply:<br /><br />* If the body is empty, both the allowed and disallowed filters are set empty.<br />* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).<br />* If only one list type is given then only that type is set. The other type is not updated.<br />* An empty \"allowed\" list means all events are allowed.<br />* An empty \"disallowed\" list means no events are disallowed.<br />* Disallowed events take precedence over allowed events if the event type is specified in both lists.

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
    api_instance = wazo_appgateway_client.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)
body = None # object | Specify which event types to allow/disallow (optional)

    try:
        # Filter application events types.
        api_response = api_instance.applications_application_name_event_filter_put(application_name, x_asterisk_id=x_asterisk_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_application_name_event_filter_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **x_asterisk_id** | **str**|  | [optional] 
 **body** | **object**| Specify which event types to allow/disallow | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response was specified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_application_name_get**
> Application applications_application_name_get(application_name, x_asterisk_id=x_asterisk_id)

Get details of an application.

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
    api_instance = wazo_appgateway_client.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Get details of an application.
        api_response = api_instance.applications_application_name_get(application_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_application_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

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

# **applications_application_name_subscription_delete**
> Application applications_application_name_subscription_delete(application_name, event_source, x_asterisk_id=x_asterisk_id)

Unsubscribe an application from an event source.

Returns the state of the application after the subscriptions have changed

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
    api_instance = wazo_appgateway_client.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
event_source = ['event_source_example'] # list[str] | URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName}
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Unsubscribe an application from an event source.
        api_response = api_instance.applications_application_name_subscription_delete(application_name, event_source, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_application_name_subscription_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **event_source** | [**list[str]**](str.md)| URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

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

# **applications_application_name_subscription_post**
> Application applications_application_name_subscription_post(application_name, event_source, x_asterisk_id=x_asterisk_id)

Subscribe an application to a event source.

Returns the state of the application after the subscriptions have changed

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
    api_instance = wazo_appgateway_client.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
event_source = ['event_source_example'] # list[str] | URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName}
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Subscribe an application to a event source.
        api_response = api_instance.applications_application_name_subscription_post(application_name, event_source, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_application_name_subscription_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application&#39;s name | 
 **event_source** | [**list[str]**](str.md)| URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Application**](Application.md)

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

# **applications_get**
> list[Application] applications_get(x_asterisk_id=x_asterisk_id)

List all applications.

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
    api_instance = wazo_appgateway_client.ApplicationsApi(api_client)
    x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List all applications.
        api_response = api_instance.applications_get(x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[Application]**](Application.md)

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

