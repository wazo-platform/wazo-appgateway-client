# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wazo_appgateway_client.api_client import ApiClient
from wazo_appgateway_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ApplicationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def applications_application_name_event_filter_put(self, application_name, **kwargs):  # noqa: E501
        """Filter application events types.  # noqa: E501

        Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:<br /><br />\"allowed\" - Specifies an allowed list of event types<br />\"disallowed\" - Specifies a disallowed list of event types<br /><br />Further, each of those key's value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:<br /><br />\"type\" - The type name of the event to filter<br /><br />The value must be the string name (case sensitive) of the event type that needs filtering. For example:<br /><br />{ \"allowed\": [ { \"type\": \"StasisStart\" }, { \"type\": \"StasisEnd\" } ] }<br /><br />As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.<br /><br />The following rules apply:<br /><br />* If the body is empty, both the allowed and disallowed filters are set empty.<br />* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).<br />* If only one list type is given then only that type is set. The other type is not updated.<br />* An empty \"allowed\" list means all events are allowed.<br />* An empty \"disallowed\" list means no events are disallowed.<br />* Disallowed events take precedence over allowed events if the event type is specified in both lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_event_filter_put(application_name, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param body: Specify which event types to allow/disallow
        :type body: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Application
        """
        kwargs['_return_http_data_only'] = True
        return self.applications_application_name_event_filter_put_with_http_info(application_name, **kwargs)  # noqa: E501

    def applications_application_name_event_filter_put_with_http_info(self, application_name, **kwargs):  # noqa: E501
        """Filter application events types.  # noqa: E501

        Allowed and/or disallowed event type filtering can be done. The body (parameter) should specify a JSON key/value object that describes the type of event filtering needed. One, or both of the following keys can be designated:<br /><br />\"allowed\" - Specifies an allowed list of event types<br />\"disallowed\" - Specifies a disallowed list of event types<br /><br />Further, each of those key's value should be a JSON array that holds zero, or more JSON key/value objects. Each of these objects must contain the following key with an associated value:<br /><br />\"type\" - The type name of the event to filter<br /><br />The value must be the string name (case sensitive) of the event type that needs filtering. For example:<br /><br />{ \"allowed\": [ { \"type\": \"StasisStart\" }, { \"type\": \"StasisEnd\" } ] }<br /><br />As this specifies only an allowed list, then only those two event type messages are sent to the application. No other event messages are sent.<br /><br />The following rules apply:<br /><br />* If the body is empty, both the allowed and disallowed filters are set empty.<br />* If both list types are given then both are set to their respective values (note, specifying an empty array for a given type sets that type to empty).<br />* If only one list type is given then only that type is set. The other type is not updated.<br />* An empty \"allowed\" list means all events are allowed.<br />* An empty \"disallowed\" list means no events are disallowed.<br />* Disallowed events take precedence over allowed events if the event type is specified in both lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_event_filter_put_with_http_info(application_name, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param body: Specify which event types to allow/disallow
        :type body: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Application, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'application_name',
            'x_asterisk_id',
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_event_filter_put" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_name' is set
        if self.api_client.client_side_validation and ('application_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_name` when calling `applications_application_name_event_filter_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in local_var_params:
            path_params['applicationName'] = local_var_params['application_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in local_var_params:
            header_params['X-Asterisk-ID'] = local_var_params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "Application",
        }

        return self.api_client.call_api(
            '/applications/{applicationName}/eventFilter', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def applications_application_name_get(self, application_name, **kwargs):  # noqa: E501
        """Get details of an application.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_get(application_name, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Application
        """
        kwargs['_return_http_data_only'] = True
        return self.applications_application_name_get_with_http_info(application_name, **kwargs)  # noqa: E501

    def applications_application_name_get_with_http_info(self, application_name, **kwargs):  # noqa: E501
        """Get details of an application.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_get_with_http_info(application_name, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Application, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'application_name',
            'x_asterisk_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_name' is set
        if self.api_client.client_side_validation and ('application_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_name` when calling `applications_application_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in local_var_params:
            path_params['applicationName'] = local_var_params['application_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in local_var_params:
            header_params['X-Asterisk-ID'] = local_var_params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "Application",
        }

        return self.api_client.call_api(
            '/applications/{applicationName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def applications_application_name_subscription_delete(self, application_name, event_source, **kwargs):  # noqa: E501
        """Unsubscribe an application from an event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_subscription_delete(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :type event_source: list[str]
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Application
        """
        kwargs['_return_http_data_only'] = True
        return self.applications_application_name_subscription_delete_with_http_info(application_name, event_source, **kwargs)  # noqa: E501

    def applications_application_name_subscription_delete_with_http_info(self, application_name, event_source, **kwargs):  # noqa: E501
        """Unsubscribe an application from an event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_subscription_delete_with_http_info(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :type event_source: list[str]
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Application, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'application_name',
            'event_source',
            'x_asterisk_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_subscription_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_name' is set
        if self.api_client.client_side_validation and ('application_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_name` when calling `applications_application_name_subscription_delete`")  # noqa: E501
        # verify the required parameter 'event_source' is set
        if self.api_client.client_side_validation and ('event_source' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_source'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_source` when calling `applications_application_name_subscription_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in local_var_params:
            path_params['applicationName'] = local_var_params['application_name']  # noqa: E501

        query_params = []
        if 'event_source' in local_var_params and local_var_params['event_source'] is not None:  # noqa: E501
            query_params.append(('eventSource', local_var_params['event_source']))  # noqa: E501
            collection_formats['eventSource'] = 'multi'  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in local_var_params:
            header_params['X-Asterisk-ID'] = local_var_params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "Application",
        }

        return self.api_client.call_api(
            '/applications/{applicationName}/subscription', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def applications_application_name_subscription_post(self, application_name, event_source, **kwargs):  # noqa: E501
        """Subscribe an application to a event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_subscription_post(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :type event_source: list[str]
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Application
        """
        kwargs['_return_http_data_only'] = True
        return self.applications_application_name_subscription_post_with_http_info(application_name, event_source, **kwargs)  # noqa: E501

    def applications_application_name_subscription_post_with_http_info(self, application_name, event_source, **kwargs):  # noqa: E501
        """Subscribe an application to a event source.  # noqa: E501

        Returns the state of the application after the subscriptions have changed  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_application_name_subscription_post_with_http_info(application_name, event_source, async_req=True)
        >>> result = thread.get()

        :param application_name: Application's name (required)
        :type application_name: str
        :param event_source: URI for event source (channel:{channelId}, bridge:{bridgeId}, endpoint:{tech}[/{resource}], deviceState:{deviceName} (required)
        :type event_source: list[str]
        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Application, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'application_name',
            'event_source',
            'x_asterisk_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_application_name_subscription_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'application_name' is set
        if self.api_client.client_side_validation and ('application_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['application_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `application_name` when calling `applications_application_name_subscription_post`")  # noqa: E501
        # verify the required parameter 'event_source' is set
        if self.api_client.client_side_validation and ('event_source' not in local_var_params or  # noqa: E501
                                                        local_var_params['event_source'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `event_source` when calling `applications_application_name_subscription_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in local_var_params:
            path_params['applicationName'] = local_var_params['application_name']  # noqa: E501

        query_params = []
        if 'event_source' in local_var_params and local_var_params['event_source'] is not None:  # noqa: E501
            query_params.append(('eventSource', local_var_params['event_source']))  # noqa: E501
            collection_formats['eventSource'] = 'multi'  # noqa: E501

        header_params = {}
        if 'x_asterisk_id' in local_var_params:
            header_params['X-Asterisk-ID'] = local_var_params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "Application",
        }

        return self.api_client.call_api(
            '/applications/{applicationName}/subscription', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def applications_get(self, **kwargs):  # noqa: E501
        """List all applications.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_get(async_req=True)
        >>> result = thread.get()

        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[Application]
        """
        kwargs['_return_http_data_only'] = True
        return self.applications_get_with_http_info(**kwargs)  # noqa: E501

    def applications_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all applications.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.applications_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param x_asterisk_id:
        :type x_asterisk_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[Application], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'x_asterisk_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method applications_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_asterisk_id' in local_var_params:
            header_params['X-Asterisk-ID'] = local_var_params['x_asterisk_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501
        
        response_types_map = {
            200: "list[Application]",
        }

        return self.api_client.call_api(
            '/applications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))