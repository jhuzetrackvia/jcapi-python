# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jcapiv1.api_client import ApiClient


class RadiusServersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def radius_servers_list(self, content_type, accept, **kwargs):  # noqa: E501
        """List Radius Servers  # noqa: E501

        This endpoint allows you to get a list of all RADIUS servers in your organization.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/radiusservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\ ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.radius_servers_list(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param str filter: A filter to apply to the query.
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :param str x_org_id: 
        :return: Radiusserverslist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.radius_servers_list_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.radius_servers_list_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def radius_servers_list_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """List Radius Servers  # noqa: E501

        This endpoint allows you to get a list of all RADIUS servers in your organization.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/radiusservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\ ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.radius_servers_list_with_http_info(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param str fields: Use a space seperated string of field parameters to include the data in the response. If omitted, the default list of fields will be returned. 
        :param str filter: A filter to apply to the query.
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str sort: Use space separated sort parameters to sort the collection. Default sort is ascending. Prefix with `-` to sort descending. 
        :param str x_org_id: 
        :return: Radiusserverslist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'fields', 'filter', 'limit', 'skip', 'sort', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method radius_servers_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `radius_servers_list`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `radius_servers_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('skip', params['skip']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/radiusservers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Radiusserverslist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def radius_servers_post(self, content_type, accept, **kwargs):  # noqa: E501
        """Create a Radius Server  # noqa: E501

        This endpoint allows you to create RADIUS servers in your organization.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/radiusservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"{test_radius}\",     \"networkSourceIp\": \"{0.0.0.0}\",     \"sharedSecret\":\"{secretpassword}\" }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.radius_servers_post(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Radiusserverpost body:
        :param str x_org_id: 
        :return: Radiusserverslist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.radius_servers_post_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.radius_servers_post_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def radius_servers_post_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """Create a Radius Server  # noqa: E501

        This endpoint allows you to create RADIUS servers in your organization.  #### Sample Request ``` curl -X POST https://console.jumpcloud.com/api/radiusservers/ \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"{test_radius}\",     \"networkSourceIp\": \"{0.0.0.0}\",     \"sharedSecret\":\"{secretpassword}\" }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.radius_servers_post_with_http_info(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Radiusserverpost body:
        :param str x_org_id: 
        :return: Radiusserverslist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method radius_servers_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `radius_servers_post`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `radius_servers_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/radiusservers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Radiusserverslist',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def radius_servers_put(self, content_type, accept, **kwargs):  # noqa: E501
        """Update Radius Servers  # noqa: E501

        This endpoint allows you to update RADIUS servers in your organization.  ####  ``` curl -X PUT https://console.jumpcloud.com/api/radiusservers/{ServerID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"{name_update}\",     \"networkSourceIp\": \"{0.0.0.0}\" }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.radius_servers_put(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Body body:
        :param str x_org_id: 
        :return: Radiusserverput
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.radius_servers_put_with_http_info(content_type, accept, **kwargs)  # noqa: E501
        else:
            (data) = self.radius_servers_put_with_http_info(content_type, accept, **kwargs)  # noqa: E501
            return data

    def radius_servers_put_with_http_info(self, content_type, accept, **kwargs):  # noqa: E501
        """Update Radius Servers  # noqa: E501

        This endpoint allows you to update RADIUS servers in your organization.  ####  ``` curl -X PUT https://console.jumpcloud.com/api/radiusservers/{ServerID} \\   -H 'Accept: application/json' \\   -H 'Content-Type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"name\": \"{name_update}\",     \"networkSourceIp\": \"{0.0.0.0}\" }' ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.radius_servers_put_with_http_info(content_type, accept, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: (required)
        :param str accept: (required)
        :param Body body:
        :param str x_org_id: 
        :return: Radiusserverput
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'body', 'x_org_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method radius_servers_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `radius_servers_put`")  # noqa: E501
        # verify the required parameter 'accept' is set
        if ('accept' not in params or
                params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `radius_servers_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/radiusservers:id', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Radiusserverput',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
