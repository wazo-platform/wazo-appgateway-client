# wazo_appgateway_client.MailboxesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mailboxes_get**](MailboxesApi.md#mailboxes_get) | **GET** /mailboxes | List all mailboxes.
[**mailboxes_mailbox_name_delete**](MailboxesApi.md#mailboxes_mailbox_name_delete) | **DELETE** /mailboxes/{mailboxName} | Destroy a mailbox.
[**mailboxes_mailbox_name_get**](MailboxesApi.md#mailboxes_mailbox_name_get) | **GET** /mailboxes/{mailboxName} | Retrieve the current state of a mailbox.
[**mailboxes_mailbox_name_put**](MailboxesApi.md#mailboxes_mailbox_name_put) | **PUT** /mailboxes/{mailboxName} | Change the state of a mailbox. (Note - implicitly creates the mailbox).


# **mailboxes_get**
> list[Mailbox] mailboxes_get(x_asterisk_id=x_asterisk_id)

List all mailboxes.

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
    api_instance = wazo_appgateway_client.MailboxesApi(api_client)
    x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # List all mailboxes.
        api_response = api_instance.mailboxes_get(x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailboxesApi->mailboxes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**list[Mailbox]**](Mailbox.md)

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

# **mailboxes_mailbox_name_delete**
> mailboxes_mailbox_name_delete(mailbox_name, x_asterisk_id=x_asterisk_id)

Destroy a mailbox.

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
    api_instance = wazo_appgateway_client.MailboxesApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | Name of the mailbox
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Destroy a mailbox.
        api_instance.mailboxes_mailbox_name_delete(mailbox_name, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling MailboxesApi->mailboxes_mailbox_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 
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

# **mailboxes_mailbox_name_get**
> Mailbox mailboxes_mailbox_name_get(mailbox_name, x_asterisk_id=x_asterisk_id)

Retrieve the current state of a mailbox.

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
    api_instance = wazo_appgateway_client.MailboxesApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | Name of the mailbox
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Retrieve the current state of a mailbox.
        api_response = api_instance.mailboxes_mailbox_name_get(mailbox_name, x_asterisk_id=x_asterisk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MailboxesApi->mailboxes_mailbox_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 
 **x_asterisk_id** | **str**|  | [optional] 

### Return type

[**Mailbox**](Mailbox.md)

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

# **mailboxes_mailbox_name_put**
> mailboxes_mailbox_name_put(mailbox_name, old_messages, new_messages, x_asterisk_id=x_asterisk_id)

Change the state of a mailbox. (Note - implicitly creates the mailbox).

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
    api_instance = wazo_appgateway_client.MailboxesApi(api_client)
    mailbox_name = 'mailbox_name_example' # str | Name of the mailbox
old_messages = 56 # int | Count of old messages in the mailbox
new_messages = 56 # int | Count of new messages in the mailbox
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)

    try:
        # Change the state of a mailbox. (Note - implicitly creates the mailbox).
        api_instance.mailboxes_mailbox_name_put(mailbox_name, old_messages, new_messages, x_asterisk_id=x_asterisk_id)
    except ApiException as e:
        print("Exception when calling MailboxesApi->mailboxes_mailbox_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 
 **old_messages** | **int**| Count of old messages in the mailbox | 
 **new_messages** | **int**| Count of new messages in the mailbox | 
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

