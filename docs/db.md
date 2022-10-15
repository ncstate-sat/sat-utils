The DB module aims to ease database connectivity issues across the stack by handling the connection string and credentialing under the hood.

### Password Related Variables

The below environment variables are required to use the PasswordStateClient class successfully.
Please ensure they are set as par of the deployment as either environment variables or kubernetes secrets.

| Variable    | Description |
| ----------- | ----------- |
| PASSWORDSTATE_API_URL | The url for the password state server. Defaults to https://password.ehps.ncsu.edu |
| PASSWORDSTATE_API_KEY | The APIkey token used for authentication. Defined for each list at by the password state administrator. |
| PASSWORDSTATE_LIST_ID | The ID of the list to search for your desired password |

### Common Password Related Errors

```
Exception has occurred: KeyError
'PASSWORDSTATE_LIST_ID'
```

You haven't specified the PASSWORDSTATE_LIST_ID environment variable.
