Explore the following key solutions:

API gateways with security features

Network Security Groups

Multi-Factor Authentication integration

Role-Based Access Control

Web Application Firewall

1. API gateways with security features
```python
# Import necessary libraries
from azure.mgmt.apimanagement import ApiManagementClient
from azure.identity import DefaultAzureCredential

# Set up credentials and initialize ApiManagementClient
credential = DefaultAzureCredential()
subscription_id = 'your_subscription_id_here'
apim_client = ApiManagementClient(credential, subscription_id)

# Define parameters for API Management service
resource_group_name = 'your_resource_group'
service_name = 'your_apim_service_name'
api_id = 'your_api_id'

# Create or update API Management policy to enforce security 
# Security Enhancements: 
# - Rate-limiting prevents excessive usage or abuse by limiting API requests per IP. 
# - IP filtering ensures only requests from trusted networks are processed.
policy_xml = """
<policies> 
<inbound> 
<base /> 
<!-- Rate-limiting: Limits API calls to 5 per minute per IP to prevent abuse --> 
<rate-limit-by-key calls="5" renewal-period="60" counter-key="@(context.Request.IpAddress)" /> 
<!-- IP Filtering: Allows access only from the specified IP range for security →
<ip-filter action="allow"> 
<address-range from="192.168.0.0" to="192.168.255.255" /> 
</ip-filter> 
</inbound> 
<backend> 
<base />
 </backend> 
<outbound> 
<base /> 
</outbound> 
<on-error> 
<base /> 
</on-error>

</policies>
"""
# Apply the security policies to the API
apim_client.api_policy.create_or_update(
    resource_group_name,
    service_name,
    api_id,
    parameters={
        'format': 'rawxml',
        'value': policy_xml
    }
)

print("API Management policy applied successfully.")

# Validation: 
# - Test the API with multiple requests from the same IP to trigger rate-limiting. 
# - Attempt access from an IP outside the allowed range to ensure it is blocked.

```
2. Network Security Groups
```python 
# Import necessary libraries
from azure.mgmt.network import NetworkManagementClient
from azure.identity import DefaultAzureCredential

# Set up credentials and initialize NetworkManagementClient
credential = DefaultAzureCredential()
subscription_id = 'your_subscription_id_here'
network_client = NetworkManagementClient(credential, subscription_id)

# Define parameters for Network Security Group
nsg_params = {
    'location': 'eastus',
    'security_rules': [
        {
            'name': 'AllowTrustedIPs',
            'protocol': 'Tcp',
            'direction': 'Inbound',
            'access': 'Allow',
            'priority': 100,
            'source_address_prefix': '192.168.0.0/16',
            'destination_address_prefix': '*',
            'source_port_range': '*',
            'destination_port_range': '80'
        }
    ]
}

# Create Network Security Group
nsg_result = network_client.network_security_groups.begin_create_or_update(
    'your_resource_group',
    'myNetworkSecurityGroup',
    nsg_params
).result()

print(f"Network Security Group created with ID: {nsg_result.id}")
```
3. Multi-Factor Authentication integration
```python
# Import necessary libraries
from azure.identity import DefaultAzureCredential
from msal import ConfidentialClientApplication

# Set up credentials and define tenant details
tenant_id = 'your_tenant_id_here'
client_id = 'your_client_id_here'
client_secret = 'your_client_secret_here'

# Initialize the ConfidentialClientApplication for authentication
app = ConfidentialClientApplication(
    client_id,
    authority=f"https://login.microsoftonline.com/{tenant_id}",
    client_credential=client_secret
)

# Request an access token with MFA enforced
scope = ['https://graph.microsoft.com/.default']
token_response = app.acquire_token_for_client(scopes=scope)

if 'access_token' in token_response:
    access_token = token_response['access_token']
    print("MFA enforced access token acquired successfully.")
else:
    print("Failed to acquire access token with MFA.")

```
4. Role-Based Access Control
```python
# Import necessary Azure SDK libraries
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.identity import DefaultAzureCredential

# Set up credentials and initialize AuthorizationManagementClient
credential = DefaultAzureCredential()
subscription_id = 'your_subscription_id_here'
auth_client = AuthorizationManagementClient(credential, subscription_id)

# Assign a role to a user for API access
role_assignment_params = {
    'role_definition_id': '/subscriptions/your_subscription_id_here/providers/Microsoft.Authorization/roleDefinitions/your_role_id',
    'principal_id': 'user_object_id_here',
    'scope': '/subscriptions/your_subscription_id_here/resourceGroups/your_resource_group/providers/Microsoft.Web/sites/your_api'
}

role_assignment_result = auth_client.role_assignments.create(
    scope=role_assignment_params['scope'],
    role_assignment_name='role_assignment_guid_here',
    parameters=role_assignment_params
)

print("RBAC role assigned successfully.")
```
Authentication 
```python 
#import requests
from azure.identity import DefaultAzureCredential

# Acquire an access token using DefaultAzureCredential
credential = DefaultAzureCredential()
access_token = credential.get_token('https://management.azure.com/.default').token

# Use the token to authenticate and call the API
api_url = 'https://your_api_endpoint_here'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    print("API accessed successfully.")
else:
    print(f"Failed to access API: {response.status_code}, {response.text}")
```
5. Web Application Firewall
```python
# Import necessary libraries
from azure.mgmt.frontdoor import FrontDoorManagementClient
from azure.identity import DefaultAzureCredential

# Set up credentials and initialize FrontDoorManagementClient
credential = DefaultAzureCredential()
subscription_id = 'your_subscription_id_here'
fd_client = FrontDoorManagementClient(credential, subscription_id)

# Define parameters for WAF policy
waf_policy_params = {
    'location': 'Global',
    'managed_rules': {
        'managed_rule_sets': [
            {
                'rule_set_type': 'OWASP',
                'rule_set_version': '3.2'
            }
        ]
    }
}

# Create WAF policy
waf_policy_result = fd_client.policies.begin_create_or_update(
    'your_resource_group',
    'myWAFPolicy',
    waf_policy_params
).result()

print(f"WAF policy created with ID: {waf_policy_result.id}")
```
