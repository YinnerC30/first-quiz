# Solution

What I would do to make my system secure taking into account the OWASP Top 10, would be to implement the following actions:

## General implementations

- Perform threat modeling and risk analysis to identify security requirements necessary for application design.
- Use secure design patterns and principles and reference architectures.
- Include security in all stages of the software development life cycle.
- Verify that applications have updates and patches, including code libraries.
- Configure security controls to safe values.
- Disable unnecessary features such as ports, services, pages, accounts, etc.
- Perform a hardening process for a secured environment.
- Maintain updates and patches, including code libraries.
- Verify that logs are generated in a format that is easy to process by log management tools.
- Ensure that log data is properly encrypted to prevent injections or attacks on the monitoring system or logs.

Note: Risks that are successfully mitigated:

- A04:2021 - Unsafe Design
- A05:2021 - Incorrect Security Configuration
- A06:2021 - Vulnerable and Outdated Components
- A08:2021 - Software and Data Integrity Failures
- A09:2021 - Logging and Monitoring Failures

## Implementations in mobile applications

- Each user must use an authentication and authorization method, so that only registered users can enter the system and only
  only registered users can enter the system and access only the resources assigned to them.
  resources assigned to them.
- Implement multifactor authentication to increase security.

Note: Risk that can be mitigated:

- A01:2021 - Loss of Access Control.

## Backend service implementations

- The backend must perform cryptography as this is where sensitive data is stored and processed.
- Validate all user input and avoid exposing session identifiers in the URL.
- Use whitelisting of allowed URLs and ports to limit allowed requests.

Note: Risks that are successfully mitigated:

- A02:2021 - Cryptographic Failures.
- A10:2021 - Forgery of Server Side Requests

## Database implementations

- Each user must use an authentication and authorization method, so that only registered users can log in to the system and access the system.
  only registered users can enter the system and access only the resources assigned to them.
  resources assigned to them.
- Limit the privileges of the database account used by the application.
- Use secure and complex passwords, and avoid storing passwords in plain text.
- Use prepared parameters and parameterized queries instead of concatenating SQL query strings.

Note: Risks that can be mitigated:

- A01:2021 - Loss of Access Control.
- A07:2021 - Identification and Authentication Failures
- A03:2021 - Injection

## Frontend service implementations

- Validate all user input, including web forms, cookies and URL parameters.
- Use input and output validation libraries.
- Use strong and complex passwords, and avoid storing passwords in plain text.
- Use secure session tokens and set appropriate expiration times.
- Validate all user input and avoid exposing session identifiers in the URL.
- Perform security tests and manual checks to identify possible weaknesses in identification and authentication.

Note: Risks that are successfully mitigated:

- A03:2021 - Injection
- A07:2021 - Identification and Authentication Failures
