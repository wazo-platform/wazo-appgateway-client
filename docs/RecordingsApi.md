# wazo_appgateway_client.RecordingsApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recordings_live_recording_name_delete**](RecordingsApi.md#recordings_live_recording_name_delete) | **DELETE** /recordings/live/{recordingName} | Stop a live recording and discard it.
[**recordings_live_recording_name_get**](RecordingsApi.md#recordings_live_recording_name_get) | **GET** /recordings/live/{recordingName} | List live recordings.
[**recordings_live_recording_name_mute_delete**](RecordingsApi.md#recordings_live_recording_name_mute_delete) | **DELETE** /recordings/live/{recordingName}/mute | Unmute a live recording.
[**recordings_live_recording_name_mute_post**](RecordingsApi.md#recordings_live_recording_name_mute_post) | **POST** /recordings/live/{recordingName}/mute | Mute a live recording.
[**recordings_live_recording_name_pause_delete**](RecordingsApi.md#recordings_live_recording_name_pause_delete) | **DELETE** /recordings/live/{recordingName}/pause | Unpause a live recording.
[**recordings_live_recording_name_pause_post**](RecordingsApi.md#recordings_live_recording_name_pause_post) | **POST** /recordings/live/{recordingName}/pause | Pause a live recording.
[**recordings_live_recording_name_stop_post**](RecordingsApi.md#recordings_live_recording_name_stop_post) | **POST** /recordings/live/{recordingName}/stop | Stop a live recording and store it.
[**recordings_stored_get**](RecordingsApi.md#recordings_stored_get) | **GET** /recordings/stored | List recordings that are complete.
[**recordings_stored_recording_name_copy_post**](RecordingsApi.md#recordings_stored_recording_name_copy_post) | **POST** /recordings/stored/{recordingName}/copy | Copy a stored recording.
[**recordings_stored_recording_name_delete**](RecordingsApi.md#recordings_stored_recording_name_delete) | **DELETE** /recordings/stored/{recordingName} | Delete a stored recording.
[**recordings_stored_recording_name_file_get**](RecordingsApi.md#recordings_stored_recording_name_file_get) | **GET** /recordings/stored/{recordingName}/file | Get the file associated with the stored recording.
[**recordings_stored_recording_name_get**](RecordingsApi.md#recordings_stored_recording_name_get) | **GET** /recordings/stored/{recordingName} | Get a stored recording&#39;s details.


# **recordings_live_recording_name_delete**
> recordings_live_recording_name_delete(recording_name, x_asterisk_id=x_asterisk_id)

Stop a live recording and discard it.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Stop a live recording and discard it.
        api_instance.recordings_live_recording_name_delete(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_live_recording_name_get**
> LiveRecording recordings_live_recording_name_get(recording_name, x_asterisk_id=x_asterisk_id)

List live recordings.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List live recordings.
        api_response = api_instance.recordings_live_recording_name_get(recording_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_live_recording_name_mute_delete**
> recordings_live_recording_name_mute_delete(recording_name, x_asterisk_id=x_asterisk_id)

Unmute a live recording.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Unmute a live recording.
        api_instance.recordings_live_recording_name_mute_delete(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_mute_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_live_recording_name_mute_post**
> recordings_live_recording_name_mute_post(recording_name, x_asterisk_id=x_asterisk_id)

Mute a live recording.

Muting a recording suspends silence detection, which will be restarted when the recording is unmuted.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Mute a live recording.
        api_instance.recordings_live_recording_name_mute_post(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_mute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_live_recording_name_pause_delete**
> recordings_live_recording_name_pause_delete(recording_name, x_asterisk_id=x_asterisk_id)

Unpause a live recording.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Unpause a live recording.
        api_instance.recordings_live_recording_name_pause_delete(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_pause_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_live_recording_name_pause_post**
> recordings_live_recording_name_pause_post(recording_name, x_asterisk_id=x_asterisk_id)

Pause a live recording.

Pausing a recording suspends silence detection, which will be restarted when the recording is unpaused. Paused time is not included in the accounting for maxDurationSeconds.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Pause a live recording.
        api_instance.recordings_live_recording_name_pause_post(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_pause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_live_recording_name_stop_post**
> recordings_live_recording_name_stop_post(recording_name, x_asterisk_id=x_asterisk_id)

Stop a live recording and store it.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Stop a live recording and store it.
        api_instance.recordings_live_recording_name_stop_post(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_live_recording_name_stop_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_stored_get**
> list[StoredRecording] recordings_stored_get(x_asterisk_id=x_asterisk_id)

List recordings that are complete.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List recordings that are complete.
        api_response = api_instance.recordings_stored_get(x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_stored_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[StoredRecording]**](StoredRecording.md)

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

# **recordings_stored_recording_name_copy_post**
> StoredRecording recordings_stored_recording_name_copy_post(recording_name, destination_recording_name, x_asterisk_id=x_asterisk_id)

Copy a stored recording.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording to copy
destination_recording_name = 'destination_recording_name_example' # str | The destination name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Copy a stored recording.
        api_response = api_instance.recordings_stored_recording_name_copy_post(recording_name, destination_recording_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_stored_recording_name_copy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording to copy | 
 **destination_recording_name** | **str**| The destination name of the recording | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**StoredRecording**](StoredRecording.md)

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

# **recordings_stored_recording_name_delete**
> recordings_stored_recording_name_delete(recording_name, x_asterisk_id=x_asterisk_id)

Delete a stored recording.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Delete a stored recording.
        api_instance.recordings_stored_recording_name_delete(recording_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_stored_recording_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
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

# **recordings_stored_recording_name_file_get**
> str recordings_stored_recording_name_file_get(recording_name, x_asterisk_id=x_asterisk_id)

Get the file associated with the stored recording.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Get the file associated with the stored recording.
        api_response = api_instance.recordings_stored_recording_name_file_get(recording_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_stored_recording_name_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

**str**

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

# **recordings_stored_recording_name_get**
> StoredRecording recordings_stored_recording_name_get(recording_name, x_asterisk_id=x_asterisk_id)

Get a stored recording's details.

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
    api_instance = wazo_appgateway_client.RecordingsApi(api_client)
    recording_name = 'recording_name_example' # str | The name of the recording
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Get a stored recording's details.
        api_response = api_instance.recordings_stored_recording_name_get(recording_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RecordingsApi->recordings_stored_recording_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_name** | **str**| The name of the recording | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**StoredRecording**](StoredRecording.md)

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

