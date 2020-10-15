# Endpoint

An external device that may offer/accept calls to/from Asterisk.  Unlike most resources, which have a single unique identifier, an endpoint is uniquely identified by the technology/resource pair.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_ids** | **list[str]** | Id&#39;s of channels associated with this endpoint | 
**resource** | **str** | Identifier of the endpoint, specific to the given technology. | 
**state** | **str** | Endpoint&#39;s state | [optional] 
**technology** | **str** | Technology of the endpoint | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


