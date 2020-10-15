# wazo_appgateway_client.EndpointsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_get**](EndpointsApi.md#endpoints_get) | **GET** /endpoints | List all endpoints.
[**endpoints_send_message_put**](EndpointsApi.md#endpoints_send_message_put) | **PUT** /endpoints/sendMessage | Send a message to some technology URI or endpoint.
[**endpoints_tech_get**](EndpointsApi.md#endpoints_tech_get) | **GET** /endpoints/{tech} | List available endoints for a given endpoint technology.
[**endpoints_tech_resource_get**](EndpointsApi.md#endpoints_tech_resource_get) | **GET** /endpoints/{tech}/{resource} | Details for an endpoint.
[**endpoints_tech_resource_send_message_put**](EndpointsApi.md#endpoints_tech_resource_send_message_put) | **PUT** /endpoints/{tech}/{resource}/sendMessage | Send a message to some endpoint in a technology.


# **endpoints_get**
> list[Endpoint] endpoints_get(x_asterisk_id=x_asterisk_id)

List all endpoints.

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
    api_instance = wazo_appgateway_client.EndpointsApi(api_client)
    x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List all endpoints.
        api_response = api_instance.endpoints_get(x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndpointsApi->endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[Endpoint]**](Endpoint.md)

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

# **endpoints_send_message_put**
> endpoints_send_message_put(to, _from, body=body, x_asterisk_id=x_asterisk_id, containers=containers)

Send a message to some technology URI or endpoint.

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
    api_instance = wazo_appgateway_client.EndpointsApi(api_client)
    to = 'to_example' # str | The endpoint resource or technology specific URI to send the message to. Valid resources are sip, pjsip, and xmpp.
_from = '_from_example' # str | The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp.
body = 'body_example' # str | The body of the message (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)
containers = wazo_appgateway_client.Containers() # Containers |  (optional)

    try:
        # Send a message to some technology URI or endpoint.
        api_instance.endpoints_send_message_put(to, _from, body=body, x_asterisk_id=x_asterisk_id, containers=containers)
    except ApiException as e:
        print("Exception when calling EndpointsApi->endpoints_send_message_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**| The endpoint resource or technology specific URI to send the message to. Valid resources are sip, pjsip, and xmpp. | 
 **_from** | **str**| The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp. | 
 **body** | **str**| The body of the message | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 
 **containers** | [**Containers**](Containers.md)|  | [optional] 

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

# **endpoints_tech_get**
> list[Endpoint] endpoints_tech_get(tech, x_asterisk_id=x_asterisk_id)

List available endoints for a given endpoint technology.

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
    api_instance = wazo_appgateway_client.EndpointsApi(api_client)
    tech = 'tech_example' # str | Technology of the endpoints (sip,iax2,...)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List available endoints for a given endpoint technology.
        api_response = api_instance.endpoints_tech_get(tech, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndpointsApi->endpoints_tech_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tech** | **str**| Technology of the endpoints (sip,iax2,...) | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[Endpoint]**](Endpoint.md)

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

# **endpoints_tech_resource_get**
> Endpoint endpoints_tech_resource_get(tech, resource, x_asterisk_id=x_asterisk_id)

Details for an endpoint.

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
    api_instance = wazo_appgateway_client.EndpointsApi(api_client)
    tech = 'tech_example' # str | Technology of the endpoint
resource = 'resource_example' # str | ID of the endpoint
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Details for an endpoint.
        api_response = api_instance.endpoints_tech_resource_get(tech, resource, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EndpointsApi->endpoints_tech_resource_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tech** | **str**| Technology of the endpoint | 
 **resource** | **str**| ID of the endpoint | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

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

# **endpoints_tech_resource_send_message_put**
> endpoints_tech_resource_send_message_put(tech, resource, _from, body=body, x_asterisk_id=x_asterisk_id, containers=containers)

Send a message to some endpoint in a technology.

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
    api_instance = wazo_appgateway_client.EndpointsApi(api_client)
    tech = 'tech_example' # str | Technology of the endpoint
resource = 'resource_example' # str | ID of the endpoint
_from = '_from_example' # str | The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp.
body = 'body_example' # str | The body of the message (optional)
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)
containers = wazo_appgateway_client.Containers() # Containers |  (optional)

    try:
        # Send a message to some endpoint in a technology.
        api_instance.endpoints_tech_resource_send_message_put(tech, resource, _from, body=body, x_asterisk_id=x_asterisk_id, containers=containers)
    except ApiException as e:
        print("Exception when calling EndpointsApi->endpoints_tech_resource_send_message_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tech** | **str**| Technology of the endpoint | 
 **resource** | **str**| ID of the endpoint | 
 **_from** | **str**| The endpoint resource or technology specific identity to send this message from. Valid resources are sip, pjsip, and xmpp. | 
 **body** | **str**| The body of the message | [optional] 
 **x_asterisk_id** | **str**|  | [optional] 
 **containers** | [**Containers**](Containers.md)|  | [optional] 

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

