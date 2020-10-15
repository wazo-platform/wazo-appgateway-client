# wazo_appgateway_client.DeviceStatesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_states_device_name_delete**](DeviceStatesApi.md#device_states_device_name_delete) | **DELETE** /deviceStates/{deviceName} | Destroy a device-state controlled by ARI.
[**device_states_device_name_get**](DeviceStatesApi.md#device_states_device_name_get) | **GET** /deviceStates/{deviceName} | Retrieve the current state of a device.
[**device_states_device_name_put**](DeviceStatesApi.md#device_states_device_name_put) | **PUT** /deviceStates/{deviceName} | Change the state of a device controlled by ARI. (Note - implicitly creates the device state).
[**device_states_get**](DeviceStatesApi.md#device_states_get) | **GET** /deviceStates | List all ARI controlled device states.


# **device_states_device_name_delete**
> device_states_device_name_delete(device_name, x_asterisk_id=x_asterisk_id)

Destroy a device-state controlled by ARI.

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
    api_instance = wazo_appgateway_client.DeviceStatesApi(api_client)
    device_name = 'device_name_example' # str | Name of the device
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Destroy a device-state controlled by ARI.
        api_instance.device_states_device_name_delete(device_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling DeviceStatesApi->device_states_device_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Name of the device | 
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

# **device_states_device_name_get**
> DeviceState device_states_device_name_get(device_name, x_asterisk_id=x_asterisk_id)

Retrieve the current state of a device.

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
    api_instance = wazo_appgateway_client.DeviceStatesApi(api_client)
    device_name = 'device_name_example' # str | Name of the device
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Retrieve the current state of a device.
        api_response = api_instance.device_states_device_name_get(device_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceStatesApi->device_states_device_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Name of the device | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**DeviceState**](DeviceState.md)

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

# **device_states_device_name_put**
> device_states_device_name_put(device_name, device_state, x_asterisk_id=x_asterisk_id)

Change the state of a device controlled by ARI. (Note - implicitly creates the device state).

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
    api_instance = wazo_appgateway_client.DeviceStatesApi(api_client)
    device_name = 'device_name_example' # str | Name of the device
device_state = 'device_state_example' # str | Device state value
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Change the state of a device controlled by ARI. (Note - implicitly creates the device state).
        api_instance.device_states_device_name_put(device_name, device_state, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling DeviceStatesApi->device_states_device_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Name of the device | 
 **device_state** | **str**| Device state value | 
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

# **device_states_get**
> list[DeviceState] device_states_get(x_asterisk_id=x_asterisk_id)

List all ARI controlled device states.

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
    api_instance = wazo_appgateway_client.DeviceStatesApi(api_client)
    x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List all ARI controlled device states.
        api_response = api_instance.device_states_get(x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeviceStatesApi->device_states_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[DeviceState]**](DeviceState.md)

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

