# coding: utf-8

"""
    Monitor API

    An API for an integrator to access the features of DocuSign Monitor  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..client.configuration import Configuration
from ..client.api_client import ApiClient


class DataSetApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_stream(self, data_set_name, version, **kwargs):
        """
        Gets customer event data for an organization.
        Gets customer event data for the organization that owns the integration key.  The results for this endpoint are paginated by event timestamp. Use the `cursor` parameter to specify where the query begins in the dataset. Use the `limit` parameter to set the number of records returned. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_stream(data_set_name, version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str data_set_name: Must be `monitor`. (required)
        :param str version: Must be `2`.  (required)
        :param str cursor: Specifies a pointer into the dataset where your query will begin. You can either provide an ISO DateTime or a string cursor (from the `endCursor` value in the response). If no value is provided, the query begins from seven days ago.  For example, to fetch event data beginning from January 1, 2022, set this value to `2022-01-01T00:00:00Z`. The response will include data about events starting from that date in chronological order. The response also includes an `endCursor` property. To fetch the next page of event data, call this endpoint again with `cursor` set to the previous `endCursor` value. 
        :param int limit: The maximum number of records to return. The default value is 1000.
        :return: CursoredResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_stream_with_http_info(data_set_name, version, **kwargs)
        else:
            (data) = self.get_stream_with_http_info(data_set_name, version, **kwargs)
            return data

    def get_stream_with_http_info(self, data_set_name, version, **kwargs):
        """
        Gets customer event data for an organization.
        Gets customer event data for the organization that owns the integration key.  The results for this endpoint are paginated by event timestamp. Use the `cursor` parameter to specify where the query begins in the dataset. Use the `limit` parameter to set the number of records returned. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_stream_with_http_info(data_set_name, version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str data_set_name: Must be `monitor`. (required)
        :param str version: Must be `2`.  (required)
        :param str cursor: Specifies a pointer into the dataset where your query will begin. You can either provide an ISO DateTime or a string cursor (from the `endCursor` value in the response). If no value is provided, the query begins from seven days ago.  For example, to fetch event data beginning from January 1, 2022, set this value to `2022-01-01T00:00:00Z`. The response will include data about events starting from that date in chronological order. The response also includes an `endCursor` property. To fetch the next page of event data, call this endpoint again with `cursor` set to the previous `endCursor` value. 
        :param int limit: The maximum number of records to return. The default value is 1000.
        :return: CursoredResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_set_name', 'version', 'cursor', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_set_name' is set
        if ('data_set_name' not in params) or (params['data_set_name'] is None):
            raise ValueError("Missing the required parameter `data_set_name` when calling `get_stream`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_stream`")


        collection_formats = {}

        resource_path = '/api/v{version}/datasets/{dataSetName}/stream'.replace('{format}', 'json')
        path_params = {}
        if 'data_set_name' in params:
            path_params['dataSetName'] = params['data_set_name']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = {}
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CursoredResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
